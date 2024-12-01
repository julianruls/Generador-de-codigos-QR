# Importamos las bibliotecas necesarias
import qrcode
import streamlit as st

# Definimos la ruta del PATH para guardar el código QR
ruta_del_path = "qr_codes/qr_code.png"

# Definimos la función que genera el código QR
def generador_qr(url, ruta_del_path):
    # Creamos el objeto QRCode con los parámetros necesarios
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # Añadimos los datos de la URL al QR
    qr.add_data(url)
    qr.make(fit=True)
    # Generamos la imagen del código QR
    img = qr.make_image(fill_color="black", back_color="white")
    # Guardamos la imagen generada en la ruta especificada
    img.save(ruta_del_path)

# Configuramos la página de Streamlit
st.set_page_config(page_title="Generador de QR", layout="centered")

# Añadimos título e interfaz
st.title("Generador de Códigos QR")
url = st.text_input("Inserte la URL aquí")

# Botón para generar el código QR
if st.button("Generar código QR"):
    if url:  # Verificamos que la URL no esté vacía
        generador_qr(url, ruta_del_path)
        # Mostramos la imagen generada
        st.image(ruta_del_path, use_container_width=True)
        # Opción para descargar la imagen
        with open(ruta_del_path, "rb") as f:
            image_data = f.read()
        st.download_button(
            label="Descargar QR",
            data=image_data,
            file_name="QRcode.png",
            mime="image/png"
        )
    else:
        st.error("Por favor, ingrese una URL válida.")
