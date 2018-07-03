from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
        "my_list": [
            {
                "restaurant_name":"Burger King",
                "food_type":"burger",
            },
            {
                "restaurant_name":"Pizza Hut",
                "food_type":"burger",
            },
            {
                "restaurant_name":"McDonalds",
                "food_type":"nuggets",
            },
        ],
    }


    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
        "my_object": {
            "restaurant_name":"Burger King",
            "food_type":"burger",
            "ingredients":"mayonnaise ketchup meat",
            "delivery":"Yes",
        },
    }
    return render(request, 'detail.html', context)
