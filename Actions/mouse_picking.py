"""
Mouse Picking Module for OpenGL
Provides functionality to convert mouse coordinates to 3D rays and perform intersection tests.

Requirements:
    - NumPy
    - PyOpenGL
"""

import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from typing import Tuple, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MousePicker:
    @staticmethod
    def get_model_view() -> np.ndarray:
        """
        Get the current ModelView matrix.
        
        Returns:
            np.ndarray: 4x4 ModelView matrix
        """
        try:
            return np.array(glGetDoublev(GL_MODELVIEW_MATRIX))
        except Exception as e:
            logger.error(f"Failed to get ModelView matrix: {e}")
            raise RuntimeError("OpenGL context error: Could not get ModelView matrix")

    @staticmethod
    def get_projection() -> np.ndarray:
        """
        Get the current Projection matrix.
        
        Returns:
            np.ndarray: 4x4 Projection matrix
        """
        try:
            return np.array(glGetDoublev(GL_PROJECTION_MATRIX))
        except Exception as e:
            logger.error(f"Failed to get Projection matrix: {e}")
            raise RuntimeError("OpenGL context error: Could not get Projection matrix")

    @staticmethod
    def get_viewport() -> np.ndarray:
        """
        Get the current viewport dimensions.
        
        Returns:
            np.ndarray: Viewport parameters [x, y, width, height]
        """
        try:
            return np.array(glGetIntegerv(GL_VIEWPORT))
        except Exception as e:
            logger.error(f"Failed to get viewport: {e}")
            raise RuntimeError("OpenGL context error: Could not get viewport")

    @classmethod
    def get_ray_from_mouse(cls, mouse_x: float, mouse_y: float) -> Tuple[np.ndarray, np.ndarray]:
        """
        Convert mouse coordinates to a ray in world space.
        
        Args:
            mouse_x (float): Mouse X coordinate in window space
            mouse_y (float): Mouse Y coordinate in window space
            
        Returns:
            Tuple[np.ndarray, np.ndarray]: Tuple containing:
                - Ray origin point (3D vector)
                - Ray direction (normalized 3D vector)
                
        Raises:
            ValueError: If mouse coordinates are invalid
            RuntimeError: If OpenGL operations fail
        """
        if not isinstance(mouse_x, (int, float)) or not isinstance(mouse_y, (int, float)):
            raise ValueError("Mouse coordinates must be numeric values")

        try:
            viewport = cls.get_viewport()
            modelview = cls.get_model_view()
            projection = cls.get_projection()

            # Convert window y coordinate to OpenGL y coordinate
            window_y = float(viewport[3] - mouse_y)

            # Get ray start point (near plane)
            start = np.array(gluUnProject(
                mouse_x, window_y, 0.0,
                modelview,
                projection,
                viewport
            ))

            # Get ray end point (far plane)
            end = np.array(gluUnProject(
                mouse_x, window_y, 1.0,
                modelview,
                projection,
                viewport
            ))

            # Calculate ray direction
            direction = end - start
            
            # Normalize direction vector, handling zero vector case
            direction_norm = np.linalg.norm(direction)
            if direction_norm < 1e-10:
                logger.warning("Ray direction vector is near zero")
                direction = np.array([0.0, 0.0, 1.0])
            else:
                direction = direction / direction_norm

            return start, direction

        except Exception as e:
            logger.error(f"Failed to create ray from mouse coordinates: {e}")
            raise RuntimeError(f"Ray creation failed: {str(e)}")

    @staticmethod
    def check_ray_box_intersection(
        ray_origin: np.ndarray,
        ray_direction: np.ndarray,
        box_min: np.ndarray,
        box_max: np.ndarray,
        epsilon: float = 1e-10
    ) -> bool:
        """
        Check if a ray intersects with an axis-aligned bounding box (AABB).
        
        Args:
            ray_origin (np.ndarray): Origin point of the ray
            ray_direction (np.ndarray): Direction vector of the ray (should be normalized)
            box_min (np.ndarray): Minimum point of the AABB
            box_max (np.ndarray): Maximum point of the AABB
            epsilon (float): Small value to prevent division by zero
            
        Returns:
            bool: True if ray intersects the box, False otherwise
            
        Raises:
            ValueError: If input vectors have incorrect dimensions or invalid values
        """
        # Input validation
        for arr, name in [(ray_origin, 'ray_origin'), (ray_direction, 'ray_direction'),
                         (box_min, 'box_min'), (box_max, 'box_max')]:
            if not isinstance(arr, np.ndarray) or arr.shape != (3,):
                raise ValueError(f"{name} must be a 3D numpy array")

        if not np.all(box_min <= box_max):
            raise ValueError("box_min must be less than or equal to box_max in all dimensions")

        try:
            # Handle divisions by zero in ray direction
            inv_dir = np.where(np.abs(ray_direction) > epsilon,
                             1.0 / ray_direction,
                             np.sign(ray_direction) * 1.0/epsilon)

            # Calculate intersection distances
            t1 = (box_min - ray_origin) * inv_dir
            t2 = (box_max - ray_origin) * inv_dir

            # Find entrance and exit distances for each axis
            tmin = np.min(np.vstack([t1, t2]), axis=0)
            tmax = np.max(np.vstack([t1, t2]), axis=0)

            # Find the latest entrance and earliest exit
            latest_entry = np.max(tmin)
            earliest_exit = np.min(tmax)

            # Check if there is a valid intersection
            return earliest_exit >= max(0, latest_entry)

        except Exception as e:
            logger.error(f"Error in ray-box intersection test: {e}")
            return False