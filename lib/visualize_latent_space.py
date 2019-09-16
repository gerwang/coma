from psbody.mesh import Mesh, MeshViewers
import readchar
import numpy as np

def visualize_latent_space(model, facedata, mesh_path=None):
    if mesh_path is not None:
        normalized_mesh = facedata.get_normalized_meshes([mesh_path])
    else:
        normalized_mesh = np.array([facedata.vertices_test[0]])

    latent_vector = model.encode(normalized_mesh)
    viewer = MeshViewers(window_width=800, window_height=800, shape=[1, 1], titlebar='Meshes')



    while(1):
        input_key = readchar.readchar()
        up_factor = 1.1
        down_factor = 0.9
        if input_key == "q":
            latent_vector[0][0] = up_factor * latent_vector[0][0]
        elif input_key == "w":
            latent_vector[0][1] = up_factor * latent_vector[0][1]
        elif input_key == "e":
            latent_vector[0][2] = up_factor * latent_vector[0][2]
        elif input_key == "r":
            latent_vector[0][3] = up_factor * latent_vector[0][3]
        elif input_key == "t":
            latent_vector[0][4] = up_factor * latent_vector[0][4]
        elif input_key == "y":
            latent_vector[0][5] = up_factor * latent_vector[0][5]
        elif input_key == "u":
            latent_vector[0][6] = up_factor * latent_vector[0][6]
        elif input_key == "i":
            latent_vector[0][7] = up_factor * latent_vector[0][7]

        elif input_key == "a":
            latent_vector[0][0] = down_factor * latent_vector[0][0]
        elif input_key == "s":
            latent_vector[0][1] = down_factor * latent_vector[0][1]
        elif input_key == "d":
            latent_vector[0][2] = down_factor * latent_vector[0][2]
        elif input_key == "f":
            latent_vector[0][3] = down_factor * latent_vector[0][3]
        elif input_key == "g":
            latent_vector[0][4] = down_factor * latent_vector[0][4]
        elif input_key == "h":
            latent_vector[0][5] = down_factor * latent_vector[0][5]
        elif input_key == "j":
            latent_vector[0][6] = down_factor * latent_vector[0][6]
        elif input_key == "k":
            latent_vector[0][7] = down_factor * latent_vector[0][7]
        elif input_key == "\x1b":
            break

        recon_vec = model.decode(latent_vector)
        facedata.show_mesh(viewer=viewer, mesh_vecs=recon_vec, figsize=(1,1))
