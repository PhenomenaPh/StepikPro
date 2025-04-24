class Config:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object().__new__(cls)
        return cls._instance

    def __init__(self):
        self.program_name = "GenerationPy"
        self.environment = "release"
        self.log_level = "verbose"
        self.version = "1.0.0"
