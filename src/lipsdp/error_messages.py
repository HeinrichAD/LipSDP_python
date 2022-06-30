import logging
import math


def cap_input(input_num, N, type):
    # Caps number of a quantity (rand_num_neurons or num_dec_vars) to
    # N choose 2 and prints information to user
    #
    # params:
    #   * input_num: int - input quantity: rand_num_neurons or num_dec_vars
    #   * N: int         - total number of hidden neurons in neural network
    #   * type: str      - name of input_num to print to user
    #
    # returns:
    #   * input_num: int - capped input number if quantity is over limit
    #                      otherwise, the original quantity is returned
    # ---------------------------------------------------------------------

    if input_num > math.comb(N, 2):
        log = logging.getLogger("lipsdp")
        log.info('Capping number of %s to %s', type, str(math.comb(N, 2)))
        log.info('Your network has %d hidden neurons and this', N)
        log.info('only allows for (%d choose 2) = %s %s.', N, str(math.comb(N, 2)), type)
        input_num = math.comb(N, 2)

    return input_num


def invalid_mode(mode):
    # Error message for invalid mode - should already be caught in Python
    #
    # params:
    #   * mode: str - formulation for LipSDP supplied by user
    # ---------------------------------------------------------------------

    error_msg = (
        'formulation must be in ' +
        '["neuron", "network", "layer", "network-rand", "network-dec-vars"]. ' +
        'You supplied formulation = ' + mode
    )
    logging.getLogger("lipsdp").error(error_msg)
    raise ValueError("[ERROR]: " + error_msg)
