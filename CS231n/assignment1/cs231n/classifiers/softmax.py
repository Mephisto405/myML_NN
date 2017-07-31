import numpy as np
from random import shuffle
from past.builtins import xrange

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  N = X.shape[0]
  loss = 0.0
  dW = np.zeros_like(W)
    
  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  # forward
  scores = X.dot(W)
  scores = scores - np.max(scores) # to avoid instability
  e = np.exp(scores)
  e /= np.sum(e, axis=1, keepdims=True)
  loss -= np.sum(np.log(e[np.arange(N), y])) # important! mask. for all i in np.arange(N), sum all log(e[i,y[i]]). (binary label = 0 or 1 only)
  loss /= N
  loss += 0.5 * reg * np.sum(W**2)

  # backward
  de = np.copy(e)
  de[np.arange(N), y] -= 1
  dW = (X.T).dot(de) # (3073 * 1000) * (1000 * 10) = (3073 * 10)
  dW /= N
  dW += reg * W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  N = X.shape[0]
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  # forward
  scores = X.dot(W)
  scores = scores - np.max(scores) # to avoid instability
  e = np.exp(scores)
  e /= np.sum(e, axis=1, keepdims=True)
  loss -= np.sum(np.log(e[np.arange(N), y])) # important! mask. for all i in np.arange(N), sum all log(e[i,y[i]]). (binary label = 0 or 1 only)
  loss /= N
  loss += 0.5 * reg * np.sum(W**2)

  # backward
  de = np.copy(e)
  de[np.arange(N), y] -= 1
  dW = (X.T).dot(de) # (3073 * 1000) * (1000 * 10) = (3073 * 10)
  dW /= N
  dW += reg * W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

