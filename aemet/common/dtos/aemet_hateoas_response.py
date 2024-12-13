
class AemetHateoasResponse:
    def __init__(self, description, status, data, metadata):
        self.description = description
        self.status = status
        self.data = data
        self.metadata = metadata

    def __repr__(self):
        return f"ApiResponse(description={self.description}, status={self.status}, data={self.data}, metadata={self.metadata})"