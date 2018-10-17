
1. sử dụng wildcard cho các từ "thừa" hoặc ít ảnh hưởng tới nghĩa của câu
    thứ tự ưu tiên từ cao đến thấp cho các wildcard là:
        # >>> * >>> MATCH_FULL_TỪ >> ^ >> _

2. Với các topic có entity thì có thể tạo các file set là thuộc tính, đặc điểm của các entity đó hoặc là tác động của môi trường bên ngoài lên entity đó

    VD: với topic 6 nói về các clb thì 
        - trường sẽ có nhiều clb -> 1 file set chứa tên clb
        - các clb có cách thức hoạt động, tuyển sinh, nội quy khác nhau ->> nhiều file map tương ứng với cách thức hoạt động, tuyển sinh ... key là tên clb (thuộc file set ở trên), value là các đặc trưng tương ứng. 
        
        - nếu các đặc điểm, tính chất của 1 clb quá nhiều và các đặc điểm này cũng tồn tại ở các clb khác thì ta có thể tạo riêng 1 set chứa các đặc điểm đó 
                vd: clb it có một số đặc điểm như:
                    nhiệm vụ
                    để làm gì
                    mục tiêu

                    được gì
                    lợi ích
                    cho 
                    giúp
                    mang lại
                    nhận được
                    ích lợi

                    học gì
                    dạy

                    không học   
                    khác ngành
                    khác trường

                với file set này ta có thể dựng được file map tương ứng về đặc điểm của clb it

        - clb sẽ phải có thành viên tham gia, thành viên clb có nhiều đặc điểm như:
            + yêu cầu để được vào clb
            + trình độ
            + thái độ
            + mục đích ....
            ta có thể dựng file set về thành viên clb và sử dụng cho các câu hỏi kiểu như:

                *)em k biết gì về lập trình liệu có thể tham gia 2 clb về cntt của trường không?
                *)em sức yếu ...
                *) ....

3. Việc sử dụng set map kết hợp với wildcard có vẻ rất thuận lợi và có thể match được những trường hợp không có sẵn trong data nhưng nếu lạm dụng wildcard nhằm rút ngắn thời gian nhập liệu aiml thì có thể gây conflict giữa các category khiến template đúng thì lại không được trả về do có độ ưu tiên thấp hơn.        

4. Với các topic nhiều dữ liệu thì cần lưu ý việc chọn từ để đưa vào set vì nếu chọn không kỹ sẽ dễ xảy ra tình trạng conflict như ở mục 3. 

5. Những câu hỏi khù khoằm thì mình vẫn bê nguyên câu, kèm theo mọt só wildcard vì chưa nghĩ ra cách hay hơn :)