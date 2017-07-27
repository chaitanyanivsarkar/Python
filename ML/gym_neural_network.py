import gym
import random
import tflearn
import numpy as np
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
from statistics import mean, median
from collections import Counter

LR = 1e-3
env = gym.make('CartPole-v0')
env.reset()
goal_steps = 500
score_requirement = 50
init_games = 10000

def rand_games():
    for episode in range(5):
        env.reset()
        for t in range(goal_steps):
            #env.render()
            action = env.action_space.sample()
            obs, reward, done, info = env.step(action)
            if done:
                break

def initial_pop():
    train_data = []
    scores = []
    accepted_scores = []
    for _ in range(init_games):
        score = 0
        game_mem = []
        prev_obs = []
        for _ in range(goal_steps):
            action = env.action_space.sample()
            obs, reward, done, info = env.step(action)
            if len(prev_obs) > 0:
                game_mem.append([prev_obs, action])
            prev_obs = obs
            score += reward
            if done:
                break
        scores.append(score)
        if score >= score_requirement:
            accepted_scores.append(score)
            for data in game_mem:
                if data[1] == 1:
                    output = [0,1]
                elif data[1] == 0:
                    output = [1,0]
                train_data.append([data[0], output])
        env.reset()
    train_data_save = np.array(train_data)
    np.save('saved.npy', train_data_save)
    print('avg accepted scores', mean(accepted_scores))
    print('median accepted scores', median(accepted_scores))
    return train_data
    
def neural_net_model(input_size, keep=0.8):
    '''
    1-input layer
    5-hiddel layers
    1-output layer
    '''
    # input layer
    network = input_data(shape=[None, input_size, 1], name='input')

    # hidden layers
    network = fully_connected(network, 128, activation='relu')
    network = dropout(network, keep, name='hidden_1')

    network = fully_connected(network, 256, activation='relu')
    network = dropout(network, keep, name='hidden_2')

    network = fully_connected(network, 512, activation='relu')
    network = dropout(network, keep, name='hidden_3')

    network = fully_connected(network, 256, activation='relu')
    network = dropout(network, keep, name='hidden_4')

    network = fully_connected(network, 128, activation='relu')
    network = dropout(network, keep, name='hidden_5')

    # output layer
    network = fully_connected(network, 2, activation='softmax')
    network = regression(network, optimizer='adam', learning_rate=LR,
                         loss='categorical_crossentropy', name='targets')

    # deep neural network model
    model = tflearn.DNN(network, tensorboard_dir='log')
    return model

def train_model(train_data, model=False):
    X = np.array([i[0] for i in train_data]).reshape(-1, len(train_data[0][0]), 1)
    y = np.array([i[1] for i in train_data])
    if not model:
        model = neural_net_model(input_size=len(X[0]))
    model.fit({'input':X}, {'targets':y}, n_epoch=5, snapshot_step=500,
              show_metric=False, run_id='OpenAiGame')
    return model

train_data = initial_pop()
model = train_model(train_data)
scores = []
choices = []
for each_game in range(10):
    score = 0
    game_mem = []
    prev_obs = []
    env.reset()
    for _ in range(goal_steps):
        env.render()
        if len(prev_obs) == 0:
            action = env.action_space.sample()
        else:
            action = np.argmax(model.predict(prev_obs.reshape(-1, len(prev_obs), 1))[0])
        choices.append(action)
        new_obs, reward, done, info = env.step(action)
        prev_obs = new_obs
        game_mem.append([new_obs, action])
        score += reward
        if done:
            break
    scores.append(score)
    
print("avg score", sum(scores)/len(scores))
print('choice 1 {}, choice0: {}'.format(choices.count(1)/len(choices),
                                        choices.count(0)/len(choices)))

