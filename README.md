# Deep Spot-it

Deep Neural Network model playing the [Dobble](https://fr.asmodee.com/fr/games/dobble/), aka [Spot it](https://www.asmodee.us/en/games/spot-it/) game.

## Running from virtualenv (with virtualenvwrapper)

```
# Create virtualenv
mkvirtualenv -r requirements.txt spotit_env
```

```
# Use virtualenv
workon spotit_env
```

```
# Run commands from Makefile
make clean prepare train
```

```
# Leave virtualenv
deactivate
```
