import numpy as np
def camera_and_slit(focal_depth,l,theta,x):
    """triangular

    Args:
        z_focal (_type_): Focal depth
        x_slit (_type_): distance between camera and slit
        theta_slit (_type_): slit angle
        x_image (_type_): location in image on camera
    """

    tt = np.tan(theta_slit)
    k = x_slit * tt / (x_image * tt + z_focal)

    return tt * np.array([x_image, z_focal])

def world2camera(theta_camera, x, x_camera):
    """_summary_

    Args:
        theta_camera (_type_): ワールド座標系におけるカメラ座標系の回転角
        x (_type_): カメラ座標系
        x_camera (_type_): ワールド座標系におけるカメラ位置
    """

    x = np.exp(-1j * theta_camera) * complex(x - x_camera)
    return np.array([x.real, x_imag])


