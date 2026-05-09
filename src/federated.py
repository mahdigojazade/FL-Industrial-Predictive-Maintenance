def federated_average(global_model,
                      model1,
                      model2,
                      model3):

    global_dict = global_model.state_dict()

    for key in global_dict.keys():

        global_dict[key] = (

            model1.state_dict()[key] +

            model2.state_dict()[key] +

            model3.state_dict()[key]

        ) / 3

    global_model.load_state_dict(global_dict)

    return global_model