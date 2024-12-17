
class AemetStation:
    def __init__(self, latitud, provincia, altitud, indicativo, nombre, indsinop, longitud):
        self.latitude = latitud
        self.province = provincia
        self.altitude = altitud
        self.indicative = indicativo
        self.name = nombre
        self.indsinop = indsinop
        self.longitude = longitud

    def __repr__(self):
        return f"AemetStation(latitude={self.latitude}, province={self.province}, altitude={self.altitude}, indicative={self.indicative}, name={self.name}, indsinop={self.indsinop}, longitude={self.longitude})"
