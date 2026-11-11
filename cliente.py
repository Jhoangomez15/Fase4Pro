import re
from entidad import EntidadSistema
from excepciones import ClienteInvalidoError


class Cliente(EntidadSistema):
    """
    Clase que representa a los clientes
    del sistema Software FJ.
    """

    def __init__(self, id_entidad, nombre, email, telefono):
        self._validar_identificacion(id_entidad)

        super().__init__(id_entidad)

        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    @staticmethod
    def _validar_identificacion(identificacion):
        if not str(identificacion).strip():
            raise ClienteInvalidoError(
                "La identificación no puede estar vacía."
            )

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ClienteInvalidoError(
                "El nombre no puede estar vacío."
            )
        self._nombre = valor.strip()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if not isinstance(valor, str):
            raise ClienteInvalidoError(
                "El correo debe ser texto."
            )

        patron = r"^[\w.+-]+@[\w-]+\.[A-Za-z]{2,}$"

        if not re.fullmatch(patron, valor.strip()):
            raise ClienteInvalidoError(
                "El correo electrónico no es válido."
            )

        self._email = valor.strip()

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        telefono = str(valor).strip()
        digitos = re.sub(r"[\s()+-]", "", telefono)

        if not digitos.isdigit() or not (7 <= len(digitos) <= 15):
            raise ClienteInvalidoError(
                "El teléfono debe tener entre 7 y 15 dígitos."
            )

        self._telefono = telefono

    def obtener_detalles(self):
        return f"Cliente: {self.nombre} ({self.email})"