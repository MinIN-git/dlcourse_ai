import numpy as np


def softmax(predictions):
    '''
    Computes probabilities from scores

    Arguments:
      predictions, np array, shape is either (N) or (batch_size, N) -
        classifier output

    Returns:
      probs, np array of the same shape as predictions - 
        probability for every class, 0..1
    '''
    # TODO implement softmax
    # Your final implementation shouldn't have any loops
    preds = predictions.copy()
    preds -= np.max(preds, axis=-1, keepdims=True)

    exp_preds = np.exp(preds)
    total_sum = np.sum(exp_preds, axis=-1, keepdims=True)

    probs = exp_preds / total_sum

    # raise Exception("Not implemented!")
    return probs


def cross_entropy_loss(probs, target_index):
    '''
    Computes cross-entropy loss

    Arguments:
      probs, np array, shape is either (N) or (batch_size, N) -
        probabilities for every class
      target_index: np array of int, shape is (1) or (batch_size) -
        index of the true class for given sample(s)

    Returns:
      loss: single value
    '''
    # TODO implement cross-entropy
    # Your final implementation shouldn't have any loops

    epsilon = 1e-10
    probs = np.clip(probs, epsilon, 1.0)

    target_index = np.array(target_index).flatten()

    if probs.ndim == 1:
        loss = -np.log(probs[target_index[0]])
    else:
        batch_size = probs.shape[0]
        loss = -np.log(probs[np.arange(batch_size), target_index])

    # raise Exception("Not implemented!")
    return np.mean(loss)


def softmax_with_cross_entropy(predictions, target_index):
    '''
    Computes softmax and cross-entropy loss for model predictions,
    including the gradient

    Arguments:
      predictions, np array, shape is either (N) or (batch_size, N) -
        classifier output
      target_index: np array of int, shape is (1) or (batch_size) -
        index of the true class for given sample(s)

    Returns:
      loss, single value - cross-entropy loss
      dprediction, np array same shape as predictions - gradient of predictions by loss value
    '''
    # TODO implement softmax with cross-entropy
    # Your final implementation shouldn't have any loops


    probs = softmax(predictions)
    loss = cross_entropy_loss(probs, target_index)
    dprediction = probs.copy()

    target_index = np.array(target_index).flatten()

    if probs.ndim == 1:
        dprediction[target_index] -= 1
    else:
        batch_size = probs.shape[0]
        dprediction[np.arange(batch_size), target_index] -= 1
        dprediction /= batch_size

    # raise Exception("Not implemented!")
    return loss, dprediction


def l2_regularization(W, reg_strength):
    '''
    Computes L2 regularization loss on weights and its gradient

    Arguments:
      W, np array - weights
      reg_strength - float value

    Returns:
      loss, single value - l2 regularization loss
      gradient, np.array same shape as W - gradient of weight by l2 loss
    '''

    # TODO: implement l2 regularization and gradient
    # Your final implementation shouldn't have any loops
    loss = reg_strength * np.sum(W ** 2)
    
    grad = 2 * reg_strength * W 
    
    # raise Exception("Not implemented!")
    return loss, grad
    

def linear_softmax(X, W, target_index):
    '''
    Performs linear classification and returns loss and gradient over W

    Arguments:
      X, np array, shape (num_batch, num_features) - batch of images
      W, np array, shape (num_features, classes) - weights
      target_index, np array, shape (num_batch) - index of target classes

    Returns:
      loss, single value - cross-entropy loss
      gradient, np.array same shape as W - gradient of weight by loss

    '''
    predictions = np.dot(X, W)

    # TODO implement prediction and gradient over W
    # Your final implementation shouldn't have any loops
    loss, dprediction = softmax_with_cross_entropy(predictions, target_index)
    dW = np.dot(X.T, dprediction)

    # raise Exception("Not implemented!")
    return loss, dW


class LinearSoftmaxClassifier():
    def __init__(self):
        self.W = None

    def fit(self, X, y, batch_size=100, learning_rate=1e-7, reg=1e-5,
            epochs=1):
        '''
        Trains linear classifier
        
        Arguments:
          X, np array (num_samples, num_features) - training data
          y, np array of int (num_samples) - labels
          batch_size, int - batch size to use
          learning_rate, float - learning rate for gradient descent
          reg, float - L2 regularization strength
          epochs, int - number of epochs
        '''

        num_train = X.shape[0]
        num_features = X.shape[1]
        num_classes = np.max(y)+1
        if self.W is None:
            self.W = 0.001 * np.random.randn(num_features, num_classes)

        loss_history = []
        for epoch in range(epochs):
            shuffled_indices = np.arange(num_train)
            np.random.shuffle(shuffled_indices)
            sections = np.arange(batch_size, num_train, batch_size)
            batches_indices = np.array_split(shuffled_indices, sections)

            # TODO implement generating batches from indices
            # Compute loss and gradients
            # Apply gradient to weights using learning rate
            # Don't forget to add both cross-entropy loss
            # and regularization!

            batch_losses = []
        
            for batch_idx in batches_indices:
                X_batch = X[batch_idx]
                y_batch = y[batch_idx]
                
                # Вычисляем потери и градиенты
                ce_loss, dW_ce = linear_softmax(X_batch, self.W, y_batch)
                reg_loss, dW_reg = l2_regularization(self.W, reg)
                
                # Суммарные потери и градиенты
                total_loss = ce_loss + reg_loss
                total_grad = dW_ce + dW_reg
                
                # Обновляем веса
                self.W -= learning_rate * total_grad
                
                batch_losses.append(total_loss)
            
            # Средние потери за эпоху
            epoch_loss = np.mean(batch_losses)
            loss_history.append(epoch_loss)


            # end
            print("Epoch %i, loss: %f" % (epoch, total_loss))

        return loss_history

    def predict(self, X):
        '''
        Produces classifier predictions on the set
       
        Arguments:
          X, np array (test_samples, num_features)

        Returns:
          y_pred, np.array of int (test_samples)
        '''
        y_pred = np.zeros(X.shape[0], dtype=np.int64)

        # TODO Implement class prediction
        # Your final implementation shouldn't have any loops
        
        scores = np.dot(X, self.W)
        y_pred = np.argmax(scores, axis=-1)

        # raise Exception("Not implemented!")
        return y_pred



                
                                                          

            

                
