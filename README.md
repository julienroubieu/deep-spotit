# Deep Spot-it

Deep Neural Network model playing the [Dobble](https://fr.asmodee.com/fr/games/dobble/), aka [Spot it](https://www.asmodee.us/en/games/spot-it/) game.

## Running from virtualenv (with virtualenvwrapper)

```
# Create virtualenv
mkvirtualenv -r requirements.txt spotit_env
```

```
# User virtualenv
workon spotit_env
```

## Running from docker

This is deprecated, it requires an OpenCV installation in the container.

```
# Start tensorflow container
docker-compose up -d
    
# Install requirements
docker exec -it spotit_tensorflow_1 pip install -r /app/requirements.txt
    
# Open Jupyter notebooks
docker logs spotit_tensorflow_1
# ... and use the URL provided
    
# Run main.py
docker exec -it spotit_tensorflow_1 python main.py
```