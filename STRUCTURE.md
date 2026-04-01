# Project Structure Guide

This document explains the reorganized structure of the Kafka 101 Learning Application.

## Directory Layout

```
kafka-101-consumers/
├── .gitignore              # Git ignore patterns (protects sensitive files)
├── LICENSE                 # MIT License
├── README.md              # Main documentation and setup guide
├── STRUCTURE.md           # This file - explains project organization
├── requirements.txt       # Python dependencies
│
├── config/
│   ├── config.ini         # Your actual credentials (gitignored, not in repo)
│   └── config.ini.example # Template for configuration
│
├── docs/
│   └── README.md          # Documentation index
│
├── src/
│   ├── __init__.py        # Makes src a Python package
│   ├── app.py             # Flask web application (producer via web UI)
│   ├── consumer.py        # Kafka consumer (receives messages)
│   └── producer.py        # Kafka producer CLI (sends messages)
│
└── templates/
    └── index.html         # Web interface HTML template
```

## Key Changes from Original Structure

### Before (Flat Structure)
```
kafka-101-consumers/
├── app.py
├── consumer.py
├── producer.py
├── config.ini
├── config.ini.example
└── templates/
    └── index.html
```

### After (Organized Structure)
- **config/**: All configuration files grouped together
- **src/**: All Python source code in one place
- **docs/**: Documentation directory for future expansion
- **templates/**: Remains at root for Flask convention

## Why This Structure?

1. **Separation of Concerns**: Configuration, code, and documentation are clearly separated
2. **Scalability**: Easy to add new modules, tests, or documentation
3. **Professional**: Follows Python project best practices
4. **GitHub-Ready**: Clean structure for public repositories
5. **Security**: Sensitive config files are clearly isolated in config/

## Running the Application

All commands now reference the new paths:

### Start Consumer
```bash
python src/consumer.py config/config.ini
```

### Start Web App
```bash
python src/app.py
```

### Use CLI Producer
```bash
python src/producer.py config/config.ini -m "Hello Kafka!"
```

## Path Updates Made

1. **src/app.py**: 
   - Config path: `config/config.ini`
   - Template folder: `../templates` (relative to src/)

2. **Command line usage**: 
   - All scripts now run from project root
   - Config file path: `config/config.ini`

3. **.gitignore**: 
   - Updated to ignore `config/config.ini`

4. **README.md**: 
   - All examples updated with new paths
   - Project structure diagram updated

## Configuration Setup

1. Copy the example config:
   ```bash
   cp config/config.ini.example config/config.ini
   ```

2. Edit `config/config.ini` with your Confluent Cloud credentials

3. The file is automatically ignored by Git (never committed)

## Adding New Features

### New Python Module
Add to `src/` directory:
```bash
touch src/new_module.py
```

### New Documentation
Add to `docs/` directory:
```bash
touch docs/new_guide.md
```

### New Configuration
Add to `config/` directory and update `.gitignore` if sensitive

## Benefits of This Structure

✅ **Clear Organization**: Easy to find files by category
✅ **Secure**: Sensitive files clearly separated
✅ **Maintainable**: Logical grouping makes updates easier
✅ **Extensible**: Simple to add new components
✅ **Professional**: Follows industry standards
✅ **GitHub-Ready**: Clean structure for collaboration

## Migration Notes

If you have an existing installation:

1. Your old `config.ini` has been moved to `config/config.ini`
2. Update any scripts or shortcuts to use new paths
3. The application functionality remains exactly the same
4. All imports and file references have been updated

## Questions?

See the main [README.md](README.md) for full setup and usage instructions.