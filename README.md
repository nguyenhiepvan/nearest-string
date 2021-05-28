# Installation

clone project and run

```shell
python setup.py develop
```
**notice**: maybe need permissions

# Usage

```shell
nearest_string <your-string> <found-in-text>
```

e.g: 
```
nearest_string "Bao_quan_trung_ga_tuoi_bang_mang_bao_chitosan" "Tạp chí Khoa học – Công nghệ Thủy sản số 01/2007 Trường Đại học Nha Trang VẤN ĐỀ NGHIÊN CỨU NGHIÊN CỨU BẢO QUẢN TRỨNG GÀ TƯƠI BẰNG MÀNG BỌC CHITOSAN KẾT HỢP PHỤ GIA PGS.TS Trần Thị Luyến Khoa Chế biến - Trường ĐH Nha Trang ThS. Lê Thanh Long Khoa CK&amp;amp;CN - Đại học Nông Lâm Huế Chitosan là một polymer sinh học được điều chế từ chitin, một thành phần quan trọng của vỏ tôm, cua có nhiều ứng dụng trong bảo quản thực phẩm do khả năng kháng khuẩn của nó. Ở nhiệt độ thường, trứng gà tươi bọc màng chitosan nồng độ 1,5% có bổ sung 0,05% Sodium Benzoate hoặc 1% Sorbitol có khả năng duy trì hạng chất lượng ở mức A đến 15-20 ngày sau khi đẻ. Trong khi đó, trứng gà tươi không qua bọc màng chỉ duy trì hạng chất lượng ở mức A không quá 5 ngày, đồng thời các chỉ tiêu chất lượng khác (hao hụt khối lượng, chỉ số màu lòng đỏ trứng) đều có biến đổi lớn hơn so với trứng có xử lý màng bọc chitosan. Kết quả nghiên cứu cũng cho thấy màng bọc không tạo cảm giác khác lạ cho người sử dụng so với trứng tươi thương phẩm cùng loại về chất lượng cảm quan bề mặt. ĐẶT VẤN ĐỀ Trứng gà tươi từ lâu được sử dụng như loại thực phẩm giàu dinh dưỡng rẻ tiền trong bữa"
```
output:
`
[
     "BẢO QUẢN TRỨNG GÀ TƯƠI BẰNG MÀNG BỌC CHITOSAN ",
     0.79120879120879,
   ]
`

# Requirements
- python >= 3.7
- numpy

# Reference

- [Levenshtein Distance](https://www.datacamp.com/community/tutorials/fuzzy-string-python)
