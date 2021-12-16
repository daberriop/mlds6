# Mejora escucha digital de clientes

## Quick start

### Clone repository
```
git clone http://github.com/jonatan-parra/mlds6.git
```

change repository

```
cd mlds6
```

### Configure environment variables

create a copy of .env.def a .env

```
cp .env.dev .env
```

create a folder to store data

```
mkdir date
```

### Install dependencies
```
poetry install
```

### Download raw data
```
make fetch-data-from-gdrive
```

### Run Preprocessing pipeline

```
make run-preprocession-pipeline
```

### Run Training pipeline

```
make run-training-pipeline
```
