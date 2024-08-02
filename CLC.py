import numpy as np

# Nhập một số nguyên
def get_input_as_float(prompt):
    user_input = input(prompt)
    return float(user_input) if user_input else 0

b = get_input_as_float("Nhập chiều rộng đáy b: ")
m = get_input_as_float("Nhập mái dốc m: ")
h = get_input_as_float("Nhập độ sâu chảy đều h: ")
i = get_input_as_float("Nhập độ dốc kênh i: ")
n = get_input_as_float("Nhập hệ số nhám n: ")
D = get_input_as_float("Nhập đường kính D: ")
p = get_input_as_float("Nhập hệ số p: ")
Q = get_input_as_float("Nhập lưu lượng Q: ")
V = get_input_as_float("Nhập vận tốc V: ")
A = get_input_as_float("Nhập diện tích A: ")
#Nếu có lưu lượng
if Q!=0: 
    #Nếu có vận tốc
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
                print("Độ rộng đáy bằng", b, "và độ sâu chảy đều bằng", h)
            #Nếu 2 nghiệm
            elif delta > 0:
                for i in range(2, 4):
                    h=(-B+np.sqrt(delta)*(-1)**i)/2/a
                    b=P-2*h*np.sqrt(1+m*m)
                    if b > 0 and h > 0:
                        print("Độ rộng đáy bằng", b, "và độ sâu chảy đều bằng", h)
                    else:
                        print("Loại vì độ rộng đáy bằng", b, "và độ sâu chảy đều bằng", h)
    # Nếu là lơi nhất thuỷ lực     
    elif b==0 and h==0 and D==0 and p==0:
        h1=Q*n*2**(2/3)
        h2=(2*np.sqrt(1+m*m)-m)*np.sqrt(i)
        h=(Q*n*2**(2/3)/(2*np.sqrt(1+m*m)-m)/np.sqrt(i))**(3/8)
        b=2*h*(np.sqrt(1+m*m)-m)
        print("Để kênh hình thang có mặt cắt lợi nhất về thuỷ lực thì h bằng", h, "và b bằng", b)
    #Nếu không thì dùng thử dần để ra độ sâu dòng đều
    else:
        y2=0
        #h_min
        h1=0
        #h_max bằng D nếu là cống còn không sẽ là 100
        h2=D if D!=0 else 100
        #Tính nQ/ căn i
        y1 = n * Q / np.sqrt(i)
        while abs(y2 - y1) > 1/10**10:
            h = (h1 + h2) / 2
            #Nếu là cống tròn
            if D!=0:
                #Nếu h cao hơn bán kính cống
                if h>D/2:
                    theta=np.arcsin((h-D/2)/D*2)*2+np.pi
                #Nếu h bé hơn bán kính cống
                else:
                    theta=-np.arcsin((D/2-h)/D*2)*2+np.pi
                A=(theta-np.sin(theta))/8*D*D
                P=theta/2*D
            #Nếu là kênh hình parabol
            elif p!=0:
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
            #Nếu là kênh thông thường
            else:
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
        print("Độ sâu chảy đều là: ", h)
#Nếu hình thang có diện tích
elif A!=0:
        beta=2*(np.sqrt(1+m*m)-m)
        h=np.sqrt(A/(beta+m))
        b=h*beta
        print("Để kênh có mặt cắt lợi nhất về thuỷ lực thì h bằng", h, "và b bằng", b)
#Nếu không có lưu lượng
else:
    #Nếu là cống tròn
    if D!=0:
        #Nếu h cao hơn bán kính cống
        if h>D/2:
            theta=np.arcsin((h-D/2)/D*2)*2+np.pi
        #Nếu h thấp hơn bán kính cống
        else:
            theta=-np.arcsin((D/2-h)/D*2)*2+np.pi
        A=(theta-np.sin(theta))/8*D*D
        P=theta/2*D
    #Nếu là kênh hình parabol
    elif p!=0:
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
    #Nếu là kênh thông thường
    elif V!=0:
        y2=0
        #h_min
        h1=0
        #h_max bằng D nếu là cống còn không sẽ là 100
        h2=D if D!=0 else 100
        #Tính nQ/ căn i
        y1 = n * V / np.sqrt(i)
        while abs(y2 - y1) > 1/10**10:
            h = (h1 + h2) / 2
            #Nếu là cống tròn
            if D!=0:
                #Nếu h cao hơn bán kính cống
                if h>D/2:
                    theta=np.arcsin((h-D/2)/D*2)*2+np.pi
                #Nếu h bé hơn bán kính cống
                else:
                    theta=-np.arcsin((D/2-h)/D*2)*2+np.pi
                A=(theta-np.sin(theta))/8*D*D
                P=theta/2*D
            #Nếu là kênh hình parabol
            elif p!=0:
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
            #Nếu là kênh thông thường
            else:
                A = (b + m * h) * h
                P = b + 2 * h * np.sqrt(1 + m * m)
            #Tính bán kính thuỷ lực
            R = A / P
            y2 = R**(2 / 3)
            
            #Hiệu chỉnh h_max
            if y2 > y1:
                h2 = h
            #Hiệu chỉnh h_min
            elif y2 < y1:
                h1 = h
        print("Độ sâu chảy đều là: ", h)
    else:
        A=(b+m*h)*h
        P=b+2*h*np.sqrt(1+m*m)
        beta=2*(np.sqrt(1+m*m)-m)
    R=A/P
    Q=1/n*A*R**(2/3)*np.sqrt(i)
    print("Lưu lượng là: ", Q, "Vận tốc là: ", Q/A)