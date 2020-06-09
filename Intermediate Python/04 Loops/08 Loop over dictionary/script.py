# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna'}

# Iterate over europe
for key, value in europe.items():
    print("the capital of {} is {}".format(key, str(value)))