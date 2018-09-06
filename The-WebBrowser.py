import webbrowser
while True :
    print('Choose any number : \n1. Open any Link\n2. Search anything\n3. Open any location on maps\n4. Open Facebook\n5. Exit')
    ch = int(input())
    if ch not in [4,5] :
        address = input('Enter Data : ')
    if ch == 1 :
        webbrowser.open(address)
    elif ch == 2 :
        webbrowser.open('https://www.google.co.in/search?dcr=0&ei=gPq1WrL8DYXYvgSjpLGwCw&q='+address+'&oq='+address+'&gs_l=psy-ab.3..0i46k1j46l2j0l9.14516.16800.0.17029.6.6.0.0.0.0.247.604.0j2j1.4.0....0...1.1.64.psy-ab..2.4.857.6..35i39k1j0i67k1j0i131k1.253.hB2m7_P652I')
    elif ch == 3 :
        webbrowser.open('www.google.com/maps/place/' + address)
    elif ch == 4 :
        webbrowser.open('www.facebook.com')
    else :
        break
