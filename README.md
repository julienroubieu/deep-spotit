# Deep Spot-it

Deep Neural Network model playing the [Dobble](https://fr.asmodee.com/fr/games/dobble/), aka [Spot it](https://www.asmodee.us/en/games/spot-it/) game.

## Running from virtualenv

```
# Create virtualenv
virtualenv spotit_env
    
# Activate virtual env
source ./spotit_env/bin/activate
    
# Install requirements
pip install -r requirements.txt
```

## Running from docker

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