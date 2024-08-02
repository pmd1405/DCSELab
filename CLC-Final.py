import numpy as np

# Nhập một số nguyên
def get_input_as_float(prompt):
    user_input = input(prompt)
    return float(user_input) if user_input else 0
mode = get_input_as_float("1. Từ lưu lượng Q ra độ sâu chảy đều h\n2. Từ độ sâu chảy đều h ra lưu lượng Q\n3. Tính toán lợi nhất về mặt thuỷ lực\nNhập dạng toán: ")

if mode == 1:
    style = get_input_as_float("1. Dạng kênh thông thường\n2. Dạng kênh Parabol\n3. Dạng cống tròn\nNhập dạng kênh: ")
    if style == 1:
        Q = get_input_as_float("Nhập lưu lượng Q: ")
        b = get_input_as_float("Nhập chiều rộng đáy b: ")
        m = get_input_as_float("Nhập mái dốc m: ")
        i = get_input_as_float("Nhập độ dốc kênh i: ")
        n = get_input_as_float("Nhập hệ số nhám n: ")
        y2 = 0
        #h_min
        h1 = 0
        #h_max bằng D nếu là cống còn không sẽ là 100
        h2 = 100
        #Tính nQ/ căn i
        y1 = n * Q / np.sqrt(i)
        while abs(y2 - y1) > 1e-10:
            h = (h1 + h2) / 2
            A = (b + m * h) * h
            P = b + 2 * h * np.sqrt(1 + m * m)
            #Tính bán kính thuỷ lực
            R = A / P
            y2 = A * R**(2 / 3)

            #Hiệu chỉnh h_max
            if y2 > y1:
                h2 = h
            #Hiệu chỉnh h_min
            elif y2 < y1:
                h1 = h
        if m == 0:
                print("===Kênh chữ nhật===")
        elif b == 0:
                print("===Kênh tam giác===")
        else:
                print("===Kênh hình thang===")
        print("Độ sâu chảy đều là: ", h)
    elif style == 2:
        Q = get_input_as_float("Nhập lưu lượng Q: ")
        i = get_input_as_float("Nhập độ dốc kênh i: ")
        n = get_input_as_float("Nhập hệ số nhám n: ")
        p = get_input_as_float("Nhập hệ số p: ")
        y2=0
        #h_min
        h1=0
        #h_max bằng D nếu là cống còn không sẽ là 100
        h2=100
        #Tính nQ/ căn i
        y1 = n * Q / np.sqrt(i)
        while abs(y2 - y1) > 1e-10:
            h = (h1 + h2) / 2
            B=2*np.sqrt(2*p*h)
            A=2/3*B*h
            if h/B<=0.15:
                P=B
            elif h/B<= 0.33:
                P=B*(1+8/3*(h*h/B/B))
            elif h/B<=2:
                P=1.78*h+0.61*B
            elif h/B >2:
                P=2*h
            #Tính bán kính thuỷ lực
            R = A / P
            y2 = A * R**(2 / 3)
            
            #Hiệu chỉnh h_max
            if y2 > y1:
                h2 = h
            #Hiệu chỉnh h_min
            elif y2 < y1:
                h1 = h
        print("===Kênh parabol===")
        print("Độ sâu chảy đều là: ", h)
    elif style == 3:
        Q = get_input_as_float("Nhập lưu lượng Q: ")
        i = get_input_as_float("Nhập độ dốc kênh i: ")
        n = get_input_as_float("Nhập hệ số nhám n: ")
        D = get_input_as_float("Nhập đường kính D: ")
        y2 = 0
        #h_min
        h1 = 0
        #h_max bằng D nếu là cống còn không sẽ là 100
        h2 = D 
        #Tính nQ/ căn i
        y1 = n * Q / np.sqrt(i)
        while abs(y2 - y1) > 1e-10:
            h = (h1 + h2) / 2
            #Nếu h cao hơn bán kính cống
            if h>D/2:
                theta=np.arcsin((h-D/2)/D*2)*2+np.pi
            #Nếu h bé hơn bán kính cống
            else:
                theta=-np.arcsin((D/2-h)/D*2)*2+np.pi
            A=(theta-np.sin(theta))/8*D*D
            P=theta/2*D
            R = A / P
            y2 = A * R**(2 / 3)
            
            #Hiệu chỉnh h_max
            if y2 > y1:
                h2 = h
            #Hiệu chỉnh h_min
            elif y2 < y1:
                h1 = h
        print("===Cống tròn===")
        print("Độ sâu chảy đều là: ", h)
elif mode == 2:
    style = get_input_as_float("1. Dạng kênh thông thường\n2. Dạng kênh Parabol\n3. Dạng cống tròn\nNhập dạng kênh: ")
    if style == 1:
        h = get_input_as_float("Nhập độ sâu chảy đều h: ")
        b = get_input_as_float("Nhập chiều rộng đáy b: ")
        m = get_input_as_float("Nhập mái dốc m: ")
        i = get_input_as_float("Nhập độ dốc kênh i: ")
        n = get_input_as_float("Nhập hệ số nhám n: ")
        A = (b + m * h) * h
        P = b + 2 * h * np.sqrt(1 + m * m)
        R = A / P
        Q=1/n*A*R**(2/3)*np.sqrt(i)
        if m == 0:
                print("===Kênh chữ nhật===")
        elif b == 0:
                print("===Kênh tam giác===")
        else:
                print("===Kênh hình thang===")
        print("Lưu lượng là: ", Q, "Vận tốc là: ", Q/A)       
    elif style == 2:
        h = get_input_as_float("Nhập độ sâu chảy đều h: ")
        p = get_input_as_float("Hệ số p: ")
        i = get_input_as_float("Nhập độ dốc kênh i: ")
        n = get_input_as_float("Nhập hệ số nhám n: ")
        B=2*np.sqrt(2*p*h)
        A=2/3*B*h
        if h/B<=0.15:
            P=B
        elif h/B<= 0.33:
            P=B*(1+8/3*(h*h/B/B))
        elif h/B<=2:
            P=1.78*h+0.61*B
        elif h/B >2:
            P=2*h
        R=A/P
        Q=1/n*A*R**(2/3)*np.sqrt(i)
        print("===Kênh parabol===")
        print("Lưu lượng là: ", Q, "Vận tốc là: ", Q/A)
    elif style == 3:
        h = get_input_as_float("Nhập độ sâu chảy đều h: ")
        D = get_input_as_float("Nhập đường kính D: ")
        i = get_input_as_float("Nhập độ dốc kênh i: ")
        n = get_input_as_float("Nhập hệ số nhám n: ")
         #Nếu h cao hơn bán kính cống
        if h>D/2:
            theta=np.arcsin((h-D/2)/D*2)*2+np.pi
        #Nếu h thấp hơn bán kính cống
        else:
            theta=-np.arcsin((D/2-h)/D*2)*2+np.pi
        A=(theta-np.sin(theta))/8*D*D
        P=theta/2*D
        R=A/P
        Q=1/n*A*R**(2/3)*np.sqrt(i)
        print("===Cống tròn===")
        print("Lưu lượng là: ", Q, "Vận tốc là: ", Q/A)
elif mode == 3:
    style = get_input_as_float("1. Dạng kênh hình thang\n2. Dạng kênh Parabol\n3. Dạng cống tròn\nNhập dạng kênh: ")
    if style == 1:
        V = get_input_as_float("Nhập vận tốc V: ")
        Q = get_input_as_float("Nhập lưu lượng Q: ")
        m = get_input_as_float("Nhập mái dốc m: ")
        i = get_input_as_float("Nhập độ dốc kênh i: ")
        n = get_input_as_float("Nhập hệ số nhám n: ")
        A = get_input_as_float("Nhập diện tích A: ")
        if V!=0:
            #Tính diện tích
            A=Q/V
            #Tính Bán kính thuỷ lực
            R=(n*V/np.sqrt(i))**(3/2)
            #Tính chu vi ước
            P=A/R
            #Suy ra hệ số c
            c=-A
            #Suy ra hệ số a
            a=-2*np.sqrt(1+m*m)+2
            #Suy ra hệ số b
            B=P
            #Tính delta
            delta=B*B-4*a*c
            #Nếu vô nghiệm
            if delta < 0:
                print("Vô nghiệm")
            #Nếu nghiệm kép
            elif delta == 0:
                h=-B/2/a
                b=P-2*h*np.sqrt(1+m*m)
                if m == 0:
                    print("===Lợi nhất về mặt thuỷ lực kênh hình chữ nhật==")
                elif b == 0:
                    print("===Lợi nhất về mặt thuỷ lực kênh hình tam giác==")
                else:
                    print("===Lợi nhất về mặt thuỷ lực kênh hình thang==")
                print("Độ rộng đáy bằng", b, "và độ sâu chảy đều bằng", h)
            #Nếu 2 nghiệm
            elif delta > 0:
                for i in range(2):
                    h=(-B+np.sqrt(delta)*(-1)**i)/2/a
                    b=P-2*h*np.sqrt(1+m*m)
                    if b > 0 and h > 0:
                        if m == 0:
                            print("===Lợi nhất về mặt thuỷ lực kênh hình chữ nhật==")
                        elif b == 0:
                            print("===Lợi nhất về mặt thuỷ lực kênh hình tam giác==")
                        else:
                            print("===Lợi nhất về mặt thuỷ lực kênh hình thang==")
                        print("Độ rộng đáy bằng", b, "và độ sâu chảy đều bằng", h)
                    else:
                        print("Loại vì độ rộng đáy bằng", b, "và độ sâu chảy đều bằng", h) 
        elif A != 0:
                beta=2*(np.sqrt(1+m*m)-m)
                h=np.sqrt(A/(beta+m))
                b=h*beta
                print("Độ rộng đáy bằng", b, "và độ sâu chảy đều bằng", h)
        else:                
            h1=Q*n*2**(2/3)
            h2=(2*np.sqrt(1+m*m)-m)*np.sqrt(i)
            h=(Q*n*2**(2/3)/(2*np.sqrt(1+m*m)-m)/np.sqrt(i))**(3/8)
            b=2*h*(np.sqrt(1+m*m)-m)        
            print("Độ rộng đáy bằng", b, "và độ sâu chảy đều bằng", h)
    elif style == 2:
        print("===Lợi nhất về mặt thuỷ lực kênh parabol==")   
        Q = get_input_as_float("Nhập lưu lượng Q: ")
        i = get_input_as_float("Nhập độ dốc kênh i: ")
        n = get_input_as_float("Nhập hệ số nhám n: ")
        beta = get_input_as_float("Nhập hệ số beta thực nghiệm (Tốt nhất hiện tại là 2.92): ")
        print("===Lợi nhất về mặt thuỷ lực kênh parabol===")
        y2 = 0
        #h_min
        h1 = 0
        #h_max bằng D nếu là cống còn không sẽ là 100
        h2 = 3
        #Tính nQ/ căn i
        y1 =  Q / np.sqrt(i) * n
        while abs(y2 - y1) > 1e-10:
            h = (h1 + h2) / 2
            B = beta*h
            A = 2 * B * h / 3
            P = 1.78*h+0.61*B
            #Tính bán kính thuỷ lực
            R = A / P
            y2 = A * R**(2 / 3)
            #Hiệu chỉnh h_max
            if y2 > y1:
                h2 = h
            #Hiệu chỉnh h_min
            elif y2 < y1:
                h1 = h
        p=(B/2)**2/2/h
        print("Hệ số p bằng", p, "với độ sâu chảy đều bằng ", h, "với diện tích bằng", A)      
    elif style == 3:
        circle = get_input_as_float("1. Cho Q tìm D nhỏ nhất\n2. Cho D tìm Q lớn nhất\nNhập dạng toán: ")
        print("===Lợi nhất về mặt thuỷ lực cống tròn===")
        if circle == 1:
            Q = get_input_as_float("Nhập lưu lượng Q: ")
            i = get_input_as_float("Nhập độ dốc kênh i: ")
            n = get_input_as_float("Nhập hệ số nhám n: ")
            Qng=Q/1.076
            AngR23=Qng*n/np.sqrt(i)
            D83=AngR23/np.pi*4*4**(2/3)
            D=D83**(3/8)
            h=D*0.938
            print("Đường kính cống tròn bằng", D, "với độ sâu dòng đều bằng", h)
        elif circle == 2:
            D = get_input_as_float("Nhập đường kính D: ")
            i = get_input_as_float("Nhập độ dốc kênh i: ")
            n = get_input_as_float("Nhập hệ số nhám n: ")
            Qng=np.sqrt(i)/n*np.pi*D*D/4*(D/4)**(2/3)
            Qmax=1.076*Qng
            h=D*0.938
            print("Lưu lượng tối đa bằng: ", Qmax, "với độ sâu dòng đều bằng", h)