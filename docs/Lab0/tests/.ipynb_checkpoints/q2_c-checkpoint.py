OK_FORMAT = True

test = {   'name': 'q2_c',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> type(array_sum(a,b)) == np.ndarray\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> (array_sum([1], [1]) == np.array([2])).all()\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> array1 = [1,2,3,4,5];\n>>> array2 = [2,4,6,8,10];\n>>> (array_sum(array1, array2) == np.array([9,68,225,528,1025])).all()\nTrue',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
