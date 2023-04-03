# deploy-auto-ml-ousadia
This GitHub repository hosts a Machine Learning project developed as part of a course at FIAP. The project's objective is to deploy an AutoML model, simulating an Ifood case, using PyCaret and Streamlit.

## Technology and Resources

- [Python 3.10](https://www.python.org/downloads/release/python-31010/)
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/)
- [Pipenv](https://github.com/pypa/pipenv)
- [Streamlit](https://streamlit.io/)

## Running locally
### How to Install

```
make local/install
```

### How to enter the virtual environment

```
make local/shell
```

### How to Run

```
make local/run
```

## Running Docker

### How to Build Docker

```
make docker/build
```

### How to Run

```
make docker/run
```

### Recommended command to running the application

```
make docker/build && make docker/run
```

**Helpful commands**

_Please, check all available commands in the [Makefile](Makefile) for more information_.
