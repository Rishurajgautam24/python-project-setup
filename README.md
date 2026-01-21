# Python Project Setup Template

A production-ready Python project template with a modular architecture, featuring separation of concerns between backend and frontend layers, factory design patterns, and configuration management.

## 🏗️ Project Structure

```
Project/
├── app.py                    # Application entry point
├── main.py                   # Alternative entry point
├── pyproject.toml           # Project dependencies and metadata
├── uv.lock                  # Dependency lock file
├── .env                     # Environment variables (not tracked)
│
├── backend/                 # Backend layer - Data processing & business logic
│   └── src/
│       ├── auth/           # Authentication modules
│       ├── computer/       # Computation modules
│       ├── data/           # Data layer with factory pattern
│       │   ├── reader/     # Data readers (CSV, Excel, etc.)
│       │   │   ├── interface.py    # IReader abstract base class
│       │   │   ├── factory.py      # DataReaderFactory
│       │   │   ├── csv.py          # CSV reader implementation
│       │   │   └── excel.py        # Excel reader implementation
│       │   └── writer/     # Data writers
│       │       ├── interface.py    # IWriter abstract base class
│       │       └── factory.py      # DataWriterFactory
│       ├── ingestor/       # Data ingestion modules
│       ├── processor/      # Data processing modules
│       └── validator/      # Data validation modules
│
├── frontend/               # Frontend layer - Application management & UI
│   └── src/
│       ├── auth/          # Frontend authentication
│       │   └── manager.py
│       ├── page/          # Page/view components
│       └── manager.py     # AppManager - main application controller
│
├── config/                # Configuration management
│   ├── name_space.py     # ConfigFactory - YAML/ENV config loader
│   └── __init__.py
│
├── data/                  # Data storage
│   ├── config/           # Configuration files
│   │   ├── config.yaml   # Application configuration
│   │   └── Schema.xlsx   # Data schema definitions
│   ├── db/               # Database files
│   ├── source/           # Source data files
│   └── ui/               # UI-related data
│
└── test/                 # Test modules
    └── __init__.py
```

## ✨ Key Features

### 🎯 Modular Architecture
- **Backend Layer**: Handles data processing, business logic, and computation
- **Frontend Layer**: Manages application flow, user interface, and presentation
- **Config Layer**: Centralized configuration management

### 🏭 Factory Design Pattern
- **DataReaderFactory**: Dynamically creates appropriate data readers (CSV, Excel, etc.)
- **DataWriterFactory**: Dynamically creates appropriate data writers
- **Interface-based Design**: Uses abstract base classes for extensibility

### ⚙️ Configuration Management
- **ConfigFactory**: Converts YAML and .env files into nested namespaces
- **Schema-driven**: Excel-based schema definitions for data validation
- **Environment Variables**: Secure credential management via `.env`

### 📦 Dependency Management
- **UV Package Manager**: Fast, modern Python package management
- **pyproject.toml**: Standard Python project configuration
- Core dependencies:
  - `pandas` - Data manipulation
  - `python-dotenv` - Environment variable management
  - `pyyaml` - YAML configuration parsing

## 🚀 Getting Started

### Prerequisites
- Python 3.14+
- UV package manager (recommended) or pip

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Project
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   
   Using UV (recommended):
   ```bash
   uv sync
   ```
   
   Using pip:
   ```bash
   pip install -e .
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env  # Create .env from example
   # Edit .env with your configuration
   ```

5. **Update configuration**
   - Edit `data/config/config.yaml` with your parameters
   - Update `data/config/Schema.xlsx` with your data schemas

## 💻 Usage

### Running the Application

```bash
python app.py
```

Or alternatively:
```bash
python main.py
```

### Using the Data Reader Factory

```python
from backend.src.data.reader.factory import DataReaderFactory
from config.name_space import ConfigFactory

# Initialize configuration
cfg = ConfigFactory(yaml_path='data/config/config.yaml').initialize()

# Create reader factory
reader_factory = DataReaderFactory(cfg)

# Read CSV file
df = reader_factory.read(source='csv', path='data/source/data.csv')

# Read Excel file
df = reader_factory.read(source='excel', path='data/source/data.xlsx', sheet_name='Sheet1')
```

### Using the Configuration System

```python
from config.name_space import ConfigFactory

# Initialize configuration
cfg = ConfigFactory(yaml_path='data/config/config.yaml').initialize()

# Access configuration values
print(cfg.Param.Name)           # Access YAML parameters
print(cfg.Secret.API_KEY)       # Access .env secrets
print(cfg.Path.ENV)             # Access path configurations
print(cfg.Schema.ACCOUNT_NAME)  # Access schema definitions
```

### Creating Custom Readers/Writers

1. **Create a new reader**:
   ```python
   from backend.src.data.reader.interface import IReader
   import pandas as pd
   
   class JSONReader(IReader):
       def read(self, path: str, **kwargs) -> pd.DataFrame:
           return pd.read_json(path, **kwargs)
   ```

2. **Register in factory**:
   ```python
   # In backend/src/data/reader/factory.py
   reader_dict = {
       'csv': CSVReader,
       'excel': ExcelReader,
       'json': JSONReader,  # Add your reader
   }
   ```

## 🏛️ Architecture Principles

### SOLID Principles
- **Single Responsibility**: Each module has one clear purpose
- **Open/Closed**: Extensible via interfaces without modifying existing code
- **Liskov Substitution**: Readers/writers are interchangeable via interfaces
- **Interface Segregation**: Minimal, focused interfaces (IReader, IWriter)
- **Dependency Inversion**: Depends on abstractions, not concrete implementations

### Design Patterns
- **Factory Pattern**: Dynamic object creation based on runtime parameters
- **Strategy Pattern**: Interchangeable reader/writer implementations
- **Namespace Pattern**: Hierarchical configuration access

## 📝 Configuration Files

### config.yaml
```yaml
Param:
  Name: 'YourAppName'
  Version: '1.0.0'

Path:
  ENV: '.env'
  DATA: 'data/source'
  OUTPUT: 'data/output'
```

### .env
```env
# API Keys
API_KEY=your_api_key_here

# Database
DB_HOST=localhost
DB_PORT=5432
DB_NAME=mydb
```

### Schema.xlsx

Excel file defining data schemas for your application. Each sheet represents a table/entity schema.

#### Sheet Naming Convention
- **Sheet names should use natural language with spaces** (e.g., "Account Name", "User Profile", "Transaction Data")
- The ConfigFactory automatically converts sheet names to two formats:
  - **UPPER_SNAKE_CASE** for schema access: `cfg.Schema.ACCOUNT_NAME`
  - **PascalCase** for column access: `cfg.Col.AccountName`

#### Required Columns

Each sheet in Schema.xlsx must have the following columns with `Variable` as the index column:

| Column Name | Type | Description | Example |
|-------------|------|-------------|---------|
| **Variable** | Index | Unique identifier for the row (index column) | `user_id`, `email`, `created_at` |
| **Name** | String | Display name or actual column name in data | `User ID`, `Email Address`, `Created At` |
| **IS Derived?** | Boolean | Whether this is a computed/derived field | `TRUE`, `FALSE` |
| **Is Read?** | Boolean | Whether this field is read from source data | `TRUE`, `FALSE` |
| **Data Type** | String | Expected data type | `int`, `str`, `datetime`, `float` |
| **Description** | String | Field description and purpose | `Unique identifier for user` |
| **Validation Rule** | String | Validation logic or constraints | `NOT NULL`, `UNIQUE`, `> 0` |

#### Example Schema.xlsx Structure

**Sheet: "Account Name"**

| Variable | Name | IS Derived? | Is Read? | Data Type | Description | Validation Rule |
|----------|------|-------------|----------|-----------|-------------|-----------------|
| account_id | Account ID | FALSE | TRUE | int | Unique account identifier | NOT NULL, UNIQUE |
| account_name | Account Name | FALSE | TRUE | str | Name of the account | NOT NULL |
| balance | Balance | FALSE | TRUE | float | Current account balance | >= 0 |
| created_at | Created At | FALSE | TRUE | datetime | Account creation timestamp | NOT NULL |
| is_active | Is Active | TRUE | FALSE | bool | Derived: balance > 0 | - |
| display_name | Display Name | TRUE | FALSE | str | Derived: account_name + account_id | - |

**Sheet: "User Profile"**

| Variable | Name | IS Derived? | Is Read? | Data Type | Description | Validation Rule |
|----------|------|-------------|----------|-----------|-------------|-----------------|
| user_id | User ID | FALSE | TRUE | int | Unique user identifier | NOT NULL, UNIQUE |
| username | Username | FALSE | TRUE | str | User's login name | NOT NULL, UNIQUE |
| email | Email | FALSE | TRUE | str | User's email address | NOT NULL, VALID EMAIL |
| full_name | Full Name | TRUE | FALSE | str | Derived: first_name + last_name | - |

#### How Schema.xlsx is Used

The ConfigFactory processes Schema.xlsx as follows:

1. **Reads all sheets** from the Excel file
2. **Creates schema dictionary** with UPPER_SNAKE_CASE keys:
   ```python
   cfg.Schema.ACCOUNT_NAME  # Full DataFrame for "Account Name" sheet
   cfg.Schema.USER_PROFILE  # Full DataFrame for "User Profile" sheet
   ```

3. **Creates column dictionary** with PascalCase keys containing only readable/derived columns:
   ```python
   cfg.Col.AccountName  # Dict of columns where IS Derived? OR Is Read? = TRUE
   cfg.Col.UserProfile  # Dict of columns where IS Derived? OR Is Read? = TRUE
   ```

#### Usage Example

```python
from config.name_space import ConfigFactory

# Initialize configuration
cfg = ConfigFactory(yaml_path='data/config/config.yaml').initialize()

# Access full schema for a table
account_schema = cfg.Schema.ACCOUNT_NAME
print(account_schema)  # Full DataFrame with all schema information

# Access specific columns for a table
account_columns = cfg.Col.AccountName
print(account_columns)  # Dict: {index: 'column_name'} for readable/derived fields

# Example: Get all readable columns
readable_cols = [
    col for idx, col in account_columns.items()
]
```

#### Best Practices

1. **Consistent Naming**: Use clear, descriptive sheet names with spaces
2. **Index Column**: Always set `Variable` as the index column in Excel
3. **Boolean Values**: Use `TRUE`/`FALSE` for IS Derived? and Is Read? columns
4. **Derived Fields**: Mark computed fields as `IS Derived? = TRUE` and `Is Read? = FALSE`
5. **Source Fields**: Mark fields from source data as `Is Read? = TRUE`
6. **Documentation**: Use Description column to document field purpose and business logic

## 🧪 Testing

```bash
# Run tests
python -m pytest test/

# Run with coverage
python -m pytest --cov=backend --cov=frontend test/
```

## 🛠️ Development

### Adding New Features

1. **Backend modules**: Add to `backend/src/`
2. **Frontend components**: Add to `frontend/src/`
3. **Configuration**: Update `config/name_space.py`
4. **Dependencies**: Add to `pyproject.toml`

### Code Style
- Follow PEP 8 guidelines
- Use type hints where applicable
- Document classes and functions with docstrings

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| pandas | ≥2.3.3 | Data manipulation and analysis |
| python-dotenv | ≥1.2.1 | Environment variable management |
| pyyaml | ≥6.0.3 | YAML configuration parsing |

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Factory pattern implementation inspired by SOLID principles
- Configuration management using modern Python best practices
- Modular architecture for scalability and maintainability

## 📧 Contact

Your Name - [@yourhandle](https://twitter.com/yourhandle)

Project Link: [https://github.com/yourusername/python-project-setup](https://github.com/yourusername/python-project-setup)

---

**Built with ❤️ using Python 3.14+**
