from unittest.mock import call


def configure_return_value(method_name, calls):
    """
    returns a function to be assigned to mock.side_effect. This side_effect
    will return the correct value for a expected call (or raise the expected
    Exception if the return value is an instance of Exception), and raise an
    AssertionError if the actual call is not an expected one.

    :param method_name: Used in the text of the AssertionError to easy debugging
    :param calls: iterable of tuples (expected_call, desired_return_value)
    :return: function to be associated to mock.side_effect
    """
    def side_effect(*args, **kwargs):
        c = call(*args, **kwargs)

        for call_args, call_result in calls:
            if c == call_args:
                if isinstance(call_result, Exception):
                    raise call_result
                return call_result
        raise AssertionError('Wrong or unexpected call to {method} '
                             '(args: {args}; kwargs: {kwargs})'.format(method=method_name,
                                                                       args=args,
                                                                       kwargs=kwargs))
    return side_effect
