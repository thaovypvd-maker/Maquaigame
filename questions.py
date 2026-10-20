# 60 câu hỏi về ma quái - yêu tinh - tín ngưỡng dân gian Việt Nam
# Mỗi câu: q (câu hỏi), options (4 đáp án), correct (index 0-3), explanation (khái niệm)

QUESTIONS = [
    # ===== NHÓM 1: MA CÓ NGUỒN GỐC TỪ CÁI CHẾT =====
    {
        "q": "Loại ma nào là người bị hổ cắn trong văn hóa dân gian?",
        "options": ["Ma trành", "Ma da", "Quỷ đói", "Hổ tinh"],
        "correct": 0,
        "explanation": "Ma trành là linh hồn của người bị hổ ăn thịt. Người này không thể siêu thoát mà trở thành nô lệ cho con hổ, đi dụ dỗ thêm người khác cho hổ bắt ăn.",
    },
    {
        "q": "Những linh hồn mất ở sông hồ được dân gian tin là sẽ thành ma gì?",
        "options": ["Ma lon", "Ma đuối", "Ma da", "Giao Long"],
        "correct": 2,
        "explanation": "Ma da là linh hồn của những người chết đuối, thường ẩn nấp ở sông, ao, hồ. Dân gian quan niệm ma da hay kéo chân người bơi lội để bắt thế mạng nhằm tìm cách siêu thoát.",
    },
    {
        "q": "Người chết do tai nạn bất đắc kỳ tử, chưa đến tuổi chết, dân gian gọi là gì?",
        "options": ["Ma trơi", "Ma lai", "Vong chưa siêu thoát", "Ma xó"],
        "correct": 2,
        "explanation": "Những người chết đột ngột, chưa hết tuổi thọ thường được tin là vong hồn còn vất vưởng, chưa thể siêu thoát, phải chờ ngày 'mãn tang' hoặc được cúng bái mới đi đầu thai.",
    },
    {
        "q": "Người chết vào giờ 'trùng tang' được dân gian tin là sẽ thành loại ma gì?",
        "options": ["Ma trùng", "Ma lai", "Quỷ đói", "Ma gà"],
        "correct": 0,
        "explanation": "Trùng tang là hiện tượng người chết vào giờ xấu, được cho là sẽ 'kéo' theo người thân trong gia đình cùng chết. Dân gian thường làm lễ trấn trùng tang để hóa giải.",
    },
    {
        "q": "Người chết mà mắt vẫn mở, dân gian tin là điều gì?",
        "options": ["Chết không nhắm mắt vì còn vướng bận", "Sẽ thành ma trơi", "Sẽ hóa thành hổ", "Đã thành thần"],
        "correct": 0,
        "explanation": "Quan niệm dân gian cho rằng người chết mà mắt không nhắm là còn vướng bận chuyện trần gian, chưa yên lòng ra đi. Thường người ta vuốt mắt cho người chết để họ được siêu thoát.",
    },
    {
        "q": "Loại ma thường được miêu tả xuất hiện trong những ngôi nhà hoang, bỏ trống lâu năm?",
        "options": ["Ma lai", "Ma xó", "Quỷ nhập tràng", "Ma trơi"],
        "correct": 0,
        "explanation": "Ma lai là một loại ma dữ, thường được cho là xuất hiện ở những nơi hoang vắng, nhà bỏ trống lâu năm, quấy nhiễu người đi đường hoặc người ngủ qua đêm.",
    },

    # ===== NHÓM 2: MA THEO VẬT NUÔI, ĐỒ VẬT =====
    {
        "q": "Loại ma được thờ cúng trong nhà để bảo vệ, canh giữ điền trạch là?",
        "options": ["Ma trơi", "Ma lai", "Ma xó", "Ma men"],
        "correct": 2,
        "explanation": "Ma xó là một loại linh hồn hoặc vong linh được nuôi dưỡng và thờ cúng trong nhà để canh giữ, bảo vệ gia trạch hoặc phục vụ cho mục đích riêng của chủ nhân.",
    },
    {
        "q": "Loại ma được cho là trú ngụ ở góc nhà, gầm giường, nơi tối tăm?",
        "options": ["Ma xó", "Ma trơi", "Ma da", "Ma trành"],
        "correct": 0,
        "explanation": "Người xưa tin rằng góc nhà, gầm giường là nơi ma xó trú ngụ. Vì vậy nhiều gia đình kiêng kỵ không ngồi lên góc giường, không quét nhà ban đêm vì sợ đuổi ma xó đi.",
    },
    {
        "q": "Con mèo đen trong dân gian thường được gắn với điềm gì?",
        "options": ["Điềm lành", "Điềm gở, ma quỷ", "Thần tài", "Sự giàu sang"],
        "correct": 1,
        "explanation": "Mèo đen trong quan niệm dân gian nhiều nơi bị coi là điềm gở, gắn với ma quỷ và bóng tối. Tuy nhiên, ở một số nền văn hóa khác, mèo đen lại là biểu tượng may mắn.",
    },
    {
        "q": "Chó trắng mũi đỏ trong dân gian thường được gắn với hình ảnh là?",
        "options": ["Chó đội nón mê", "Quỷ đầu cẩu", "Cẩu huyết", "Tất cả đáp án trên"],
        "correct": 0,
        "explanation": "Chó đội nón mê là một sinh vật hoặc điềm gở mang tính truyền thuyết và tín ngưỡng dân gian lâu đời tại Việt Nam, đặc biệt là vùng đồng quê Bắc Bộ.",
    },
    {
        "q": "Tiếng chó sủa ban đêm không rõ hướng, dân gian tin là gì?",
        "options": ["Chó nhìn thấy ma", "Trời sắp mưa", "Có trộm", "Điềm lành"],
        "correct": 0,
        "explanation": "Dân gian quan niệm chó có khả năng nhìn thấy những thứ mà mắt người không thấy được, nên khi chó sủa vô cớ ban đêm, người ta tin rằng có ma quỷ hoặc vong hồn đang đi ngang qua.",
    },
    {
        "q": "Con rắn hổ mang chúa thường gắn với điển tích nào trong dân gian?",
        "options": ["Rắn thần báo oán", "Thần tài", "Thần nông", "Thổ địa"],
        "correct": 0,
        "explanation": "Nhiều điển tích dân gian kể về rắn thần, rắn hổ mang chúa hiện về báo oán hoặc trả thù những người đã từng hại rắn. Đây là biểu tượng của oan hồn không siêu thoát.",
    },

    # ===== NHÓM 3: HIỆN TƯỢNG TỰ NHIÊN =====
    {
        "q": "Loại ma có hình dạng là một đám lửa xanh?",
        "options": ["Ma giấu", "Ma đói - ngạ quỷ", "Thần trùng", "Ma trơi"],
        "correct": 3,
        "explanation": "Ma trơi là hiện tượng các đốm lửa nhỏ, lập lòe màu xanh nhạt, trắng, đỏ hoặc vàng thường xuất hiện vào ban đêm ở các khu vực như nghĩa trang, bãi tha ma hay đầm lầy.",
    },
    {
        "q": "Hiện tượng ma trơi thực chất được khoa học lý giải là do khí gì bốc lên?",
        "options": ["Oxy", "Photpho hidro (PH3)", "Cacbon dioxit", "Nito"],
        "correct": 1,
        "explanation": "Ma trơi thực chất là khí photpho hidro (PH3) và điphotpho tetrahydrua (P2H4) bốc lên từ các chất hữu cơ phân hủy ở nghĩa trang, đầm lầy, gặp oxy trong không khí thì tự cháy, phát sáng xanh.",
    },
    {
        "q": "Ánh sáng ma quái xuất hiện gần nghĩa trang, bãi tha ma thường gọi là gì?",
        "options": ["Ma trơi", "Cầu vồng đêm", "Sương mù", "Hào quang"],
        "correct": 0,
        "explanation": "Dân gian gọi ánh sáng lập lòe ở nghĩa trang là ma trơi. Người xưa tin đó là linh hồn người chết hiện về, còn khoa học giải thích là hiện tượng hóa học của khí photpho.",
    },
    {
        "q": "Hiện tượng 'sương mù dày đặc' ở vùng núi được dân gian gắn với loại ma nào?",
        "options": ["Ma sương", "Ma lai", "Ma trơi", "Ma xó"],
        "correct": 0,
        "explanation": "Sương mù dày đặc ở vùng núi thường được dân gian gọi là 'ma sương' — người đi rừng tin rằng sương mù có thể làm lạc đường, mất phương hướng như bị ma che mắt.",
    },
    {
        "q": "Tiếng gió hú ban đêm được dân gian gọi là gì?",
        "options": ["Tiếng ma gào", "Tiếng cú kêu", "Tiếng sói hú", "Tiếng thần linh"],
        "correct": 0,
        "explanation": "Tiếng gió hú qua khe cửa, hang đá, rừng cây ban đêm thường được dân gian gọi là 'ma gào' hoặc 'tiếng quỷ khóc'. Thực chất đó chỉ là hiện tượng cộng hưởng âm thanh tự nhiên.",
    },

    # ===== NHÓM 4: MA THEO VÙNG MIỀN =====
    {
        "q": "Một dạng quỷ hút máu trong văn hóa tín ngưỡng Tây Bắc là?",
        "options": ["Ma cà rồng", "Ma cà chua", "Ma cà tím", "Phí phông"],
        "correct": 3,
        "explanation": "Trong thế giới quan của người Thái, Phí Phông được xem là một dạng quỷ hút máu hoặc kết hợp giữa xác người và hồn ma.",
    },
    {
        "q": "Loài thủy quái có hình dạng giống rồng trong dân gian là?",
        "options": ["Thuồng luồng", "Long vương", "Lông bông", "Ma da"],
        "correct": 0,
        "explanation": "Thuồng luồng là một loài thủy quái huyền thoại trong văn hóa dân gian Việt Nam và Á Đông. Được mô tả là hung dữ, có sức mạnh lớn, thường lật úp ghe thuyền hoặc bắt người hại dân vùng sông nước.",
    },
    {
        "q": "Con 'giao long' trong truyền thuyết dân gian thực chất là loài gì?",
        "options": ["Cá sấu", "Rắn nước lớn", "Rồng thật", "Cá chép hóa rồng"],
        "correct": 1,
        "explanation": "Giao long là tên gọi dân gian chỉ loài rắn nước lớn, hoặc cá sấu, được thần thoại hóa thành rồng. Truyền thuyết Lạc Long Quân - Âu Cơ có nhắc đến giao long.",
    },
    {
        "q": "Ma da thường được dân gian miêu tả có đặc điểm gì?",
        "options": ["Da xanh, tóc dài, ngồi bờ sông", "Đầu trâu mặt ngựa", "Mình người đầu hổ", "Chỉ có một mắt"],
        "correct": 0,
        "explanation": "Ma da thường được miêu tả là người phụ nữ da xanh, tóc dài, ngồi bờ sông kéo chân người bơi. Đây là hiện thân của những người chết đuối không siêu thoát.",
    },
    {
        "q": "Ở Nam Bộ, loại ma nào thường được cho là xuất hiện ở rừng tràm, đầm lầy?",
        "options": ["Ma trơi", "Ma da", "Ma rừng", "Ma xó"],
        "correct": 2,
        "explanation": "Ma rừng là cách gọi dân gian ở Nam Bộ chỉ những linh hồn vất vưởng ở rừng tràm, đầm lầy. Người đi rừng thường kiêng gọi tên, kiêng nói to để không 'động' đến ma rừng.",
    },

    # ===== NHÓM 5: YÊU TINH - TINH QUÁI =====
    {
        "q": "Một yêu quái là một cây chiên đàn cổ thụ, ngàn năm thành yêu quái đó là?",
        "options": ["Hồ ly tinh", "Mộc tinh - quỷ xương cuồng", "Tinh tinh", "Xà tinh"],
        "correct": 1,
        "explanation": "Mộc tinh hay còn gọi là quỷ xương cuồng là một yêu quái nổi tiếng trong truyền thuyết và thần thoại dân gian Việt Nam từ thời thượng cổ, thời đại Kinh Dương Vương đến thời Đinh Tiên Hoàng.",
    },
    {
        "q": "Quỷ xương cuồng được truyền thuyết mô tả có hình dạng như thế nào?",
        "options": ["Một đám xương trắng biết đi", "Một con rồng đen", "Một cô gái tóc dài", "Một ông già râu trắng"],
        "correct": 0,
        "explanation": "Quỷ xương cuồng được mô tả là một đám xương trắng biết đi, không đầu, không chân, thường xuất hiện ở nơi rừng núi hoang vu. Truyền thuyết kể nó bị diệt bởi các vị thần thời Hùng Vương.",
    },
    {
        "q": "Hồ ly tinh trong dân gian Việt Nam thường được mô tả là con vật gì hóa thành?",
        "options": ["Cáo", "Mèo", "Chó", "Rắn"],
        "correct": 0,
        "explanation": "Hồ ly tinh là cáo già tu luyện lâu năm hóa thành người, thường là người phụ nữ đẹp quyến rũ đàn ông để hút sinh khí. Truyền thuyết hồ ly tinh phổ biến ở cả Việt Nam và Trung Quốc.",
    },
    {
        "q": "Con 'thần trùng' trong dân gian là loại ma gì?",
        "options": ["Ma báo oán", "Ma trơi", "Quỷ dữ", "Thần hộ mệnh"],
        "correct": 0,
        "explanation": "Thần trùng là một loại ma báo oán trong tín ngưỡng dân gian, thường được cho là oan hồn của người chết oan ức, tìm cách trả thù người đã hại mình.",
    },
    {
        "q": "Loài 'tinh tinh' trong dân gian là gì?",
        "options": ["Một loài yêu tinh", "Con khỉ", "Con vượn", "Con dơi"],
        "correct": 0,
        "explanation": "Tinh tinh là cách gọi dân gian chỉ một loại yêu tinh hoặc con vật đã tu luyện thành tinh, thường xuất hiện trong các câu chuyện cổ tích, truyền thuyết.",
    },
    {
        "q": "Xà tinh trong dân gian là loài gì hóa thành?",
        "options": ["Rắn", "Rùa", "Cá", "Chim"],
        "correct": 0,
        "explanation": "Xà tinh là rắn già tu luyện lâu năm hóa thành yêu tinh, có thể biến thành người. Truyền thuyết xà tinh phổ biến ở nhiều nền văn hóa Á Đông, trong đó có Việt Nam.",
    },
    {
        "q": "Con 'thuồng luồng' trong dân gian có đặc điểm gì đặc biệt?",
        "options": ["Có mào đỏ trên đầu", "Có sừng", "Có cánh", "Có hai đuôi"],
        "correct": 0,
        "explanation": "Thuồng luồng được miêu tả có mào đỏ trên đầu, thân hình rắn lớn, sống ở sông hồ, có thể lật thuyền và hại người. Đây là loài thủy quái đáng sợ trong tâm thức dân gian.",
    },

    # ===== NHÓM 6: QUỶ ĐÓI - NGẠ QUỶ =====
    {
        "q": "Quỷ đói trong quan niệm dân gian là những linh hồn như thế nào?",
        "options": ["Người chết vì đói", "Người chết vì bệnh", "Người chết vì tai nạn", "Người chết vì chiến tranh"],
        "correct": 0,
        "explanation": "Quỷ đói (ngạ quỷ) là những linh hồn người chết vì đói khát, hoặc do tham lam, không biết chia sẻ khi còn sống. Chúng không thể ăn uống, cổ họng nhỏ như kim, miệng phun lửa.",
    },
    {
        "q": "Lễ cúng 'cô hồn' trong dân gian thường được tổ chức vào ngày nào âm lịch?",
        "options": ["Rằm tháng 7", "Mùng 1 Tết", "Rằm tháng Giêng", "Ngày 23 tháng Chạp"],
        "correct": 0,
        "explanation": "Rằm tháng 7 âm lịch là ngày 'xá tội vong nhân', dân gian làm lễ cúng cô hồn để bố thí cho những linh hồn không nơi nương tựa, không người thờ cúng.",
    },
    {
        "q": "Người ta thường cúng gì cho quỷ đói trong dân gian?",
        "options": ["Cháo trắng, muối gạo", "Thịt mặn", "Bánh chưng", "Trái cây"],
        "correct": 0,
        "explanation": "Cháo trắng và muối gạo là lễ vật dân gian dùng để cúng cô hồn, quỷ đói. Cháo loãng tượng trưng cho việc dễ tiêu hóa với cổ họng nhỏ của ngạ quỷ, muối gạo để xua tà khí.",
    },
    {
        "q": "Theo Phật giáo, quỷ đói (ngạ quỷ) thuộc cõi nào?",
        "options": ["Cõi ngạ quỷ", "Cõi người", "Cõi trời", "Cõi súc sinh"],
        "correct": 0,
        "explanation": "Trong Phật giáo, ngạ quỷ là một trong ba cõi ác (địa ngục, ngạ quỷ, súc sinh). Chúng sinh ở cõi này luôn đói khát nhưng không thể ăn uống, do nghiệp tham lam keo kiệt khi còn sống.",
    },

    # ===== NHÓM 7: QUỶ TRONG TÍN NGƯỠNG PHẬT GIÁO =====
    {
        "q": "Một loài quỷ có nguồn gốc từ Phật Giáo của Ấn Độ, đóng vai trò canh giữ, bảo vệ chùa chiền là?",
        "options": ["Quỷ đói", "Quỷ đầu cẩu", "Quỷ vương", "Quỷ dạ xoa - Yaksha"],
        "correct": 3,
        "explanation": "Quỷ Dạ Xoa là một chủng loại linh thể hoặc quỷ thần có nguồn gốc từ thần thoại Ấn Độ cổ đại, sau này được du nhập và tiếp biến trong văn hóa Phật giáo, Bà-la-môn giáo và dân gian Á Đông.",
    },
    {
        "q": "Quỷ Dạ Xoa thường được tạc tượng ở đâu trong chùa?",
        "options": ["Cổng chùa, hai bên bậc thềm", "Trong chính điện", "Trên mái chùa", "Dưới gốc cây"],
        "correct": 0,
        "explanation": "Tượng quỷ Dạ Xoa thường được tạc ở cổng chùa, hai bên bậc thềm với vẻ mặt dữ tợn để canh giữ, xua đuổi tà ma, bảo vệ không gian linh thiêng của chùa.",
    },
    {
        "q": "Quỷ La Sát trong Phật giáo có nguồn gốc từ đâu?",
        "options": ["Ấn Độ", "Trung Quốc", "Nhật Bản", "Việt Nam"],
        "correct": 0,
        "explanation": "Quỷ La Sát (Rakshasa) có nguồn gốc từ thần thoại Ấn Độ, sau du nhập vào Phật giáo. Chúng được mô tả là những ác quỷ hung dữ, thường xuất hiện trong kinh điển Phật giáo.",
    },
    {
        "q": "Quỷ đầu trâu mặt ngựa trong tín ngưỡng dân gian làm nhiệm vụ gì?",
        "options": ["Dẫn hồn người chết xuống âm phủ", "Canh giữ cổng chùa", "Bảo vệ nhà cửa", "Mang tài lộc đến"],
        "correct": 0,
        "explanation": "Đầu trâu (Ngưu Đầu) và mặt ngựa (Mã Diện) là hai quỷ sai dưới quyền Diêm Vương, có nhiệm vụ dẫn hồn người chết xuống âm phủ, thường được thờ trong các đền thờ âm phủ.",
    },

    # ===== NHÓM 8: TÍN NGƯỠNG THỜ CÚNG =====
    {
        "q": "Người ta thường thắp hương vào giờ nào trong ngày để cúng ma quỷ?",
        "options": ["Giờ Dậu (17-19h)", "Giờ Tý (23-1h)", "Giờ Ngọ (11-13h)", "Giờ Mão (5-7h)"],
        "correct": 0,
        "explanation": "Dân gian thường cúng cô hồn, ma quỷ vào buổi chiều tối (giờ Dậu) vì tin rằng đó là lúc âm khí bắt đầu mạnh lên. Cúng ban ngày thường dành cho thần linh, tổ tiên.",
    },
    {
        "q": "Bàn thờ 'ông Địa' trong nhà có vai trò gì?",
        "options": ["Cai quản đất đai, nhà cửa", "Cai quản bếp núc", "Cai quản tài lộc", "Cai quản giấc ngủ"],
        "correct": 0,
        "explanation": "Ông Địa (Thổ Công) là vị thần cai quản đất đai, nhà cửa, đất ở. Dân gian tin rằng ông Địa trấn giữ, xua đuổi tà ma, bảo vệ bình yên cho gia đình.",
    },
    {
        "q": "Lễ 'cúng đất' khi làm nhà mới nhằm mục đích gì?",
        "options": ["Xin phép thần linh, đuổi tà ma", "Cầu tài lộc", "Cầu sức khỏe", "Cầu duyên"],
        "correct": 0,
        "explanation": "Cúng đất khi làm nhà là nghi lễ xin phép thần linh, thổ địa và đuổi tà ma khỏi khu đất, đảm bảo gia đình sống yên ổn, không bị quấy nhiễu.",
    },
    {
        "q": "Người ta thường treo gương trong nhà để làm gì theo tín ngưỡng dân gian?",
        "options": ["Xua đuổi tà ma", "Trang trí", "Soi gương", "Cầu may"],
        "correct": 0,
        "explanation": "Gương được dân gian tin là có khả năng phản chiếu, xua đuổi tà ma, quỷ dữ. Nhiều gia đình treo gương bát quái trước cửa nhà để trấn yểm.",
    },
    {
        "q": "Bùa chú trong dân gian thường được làm từ chất liệu gì?",
        "options": ["Giấy vàng, vải đỏ", "Gỗ đào", "Đá núi", "Kim loại quý"],
        "correct": 0,
        "explanation": "Bùa chú dân gian thường được vẽ trên giấy vàng, vải đỏ, hoặc khắc lên gỗ đào. Mỗi loại có công dụng riêng: giấy vàng trấn tà, gỗ đào trừ ma, vải đỏ cầu may.",
    },
    {
        "q": "Cây đào trong dân gian có tác dụng gì theo tín ngưỡng?",
        "options": ["Trừ tà ma", "Cầu tài lộc", "Cầu duyên", "Chữa bệnh"],
        "correct": 0,
        "explanation": "Cây đào được dân gian tin là có khả năng trừ tà ma, xua đuổi điều xấu. Vào dịp Tết, người ta thường cắm cành đào trong nhà để xua đuổi tà khí năm cũ.",
    },
    {
        "q": "Muối trong tín ngưỡng dân gian có tác dụng gì?",
        "options": ["Xua đuổi tà ma", "Cầu tài lộc", "Chữa bệnh", "Làm đẹp"],
        "correct": 0,
        "explanation": "Muối được dân gian tin là có khả năng thanh tẩy, xua đuổi tà ma. Nhiều người rắc muối quanh nhà, hoặc bỏ muối vào túi áo khi đi đêm để tránh ma quỷ.",
    },

    # ===== NHÓM 9: MA TRONG ĐỜI SỐNG =====
    {
        "q": "Một loại ma hay được dùng để chửi người khác?",
        "options": ["Ma lai", "Ma gà", "Âm binh", "Quỷ nhập tràng"],
        "correct": 2,
        "explanation": "Âm binh thường bao gồm các vong hồn chưa siêu thoát, oan hồn, linh hồn binh lính tử trận, hoặc các cô hồn vất vưởng được các thầy phù thủy, pháp sư, thầy cúng chiêu mộ và sai khiến.",
    },
    {
        "q": "Loại ma nào thường được nhắc đến trong câu 'ma men'?",
        "options": ["Người nghiện rượu", "Quỷ rượu", "Thần rượu", "Ma trơi"],
        "correct": 0,
        "explanation": "'Ma men' là cách nói dân gian chỉ những người nghiện rượu, uống rượu say không kiểm soát. Từ 'ma' ở đây mang nghĩa ẩn dụ, không phải ma quỷ thật.",
    },
    {
        "q": "Câu 'ma cũ bắt nạt ma mới' thường dùng để chỉ điều gì?",
        "options": ["Người mới bị bắt nạt", "Ma quỷ cãi nhau", "Người cũ ghen tị", "Sự may mắn"],
        "correct": 0,
        "explanation": "Thành ngữ 'ma cũ bắt nạt ma mới' dùng để chỉ hiện tượng người mới đến thường bị người cũ bắt nạt, ức hiếp. 'Ma' ở đây là cách nói ẩn dụ, không phải ma quỷ thật.",
    },
    {
        "q": "Người ta thường nói 'ma xui quỷ khiến' khi nào?",
        "options": ["Khi làm điều gì đó không kiểm soát", "Khi gặp may mắn", "Khi gặp ma thật", "Khi đi chùa"],
        "correct": 0,
        "explanation": "Câu 'ma xui quỷ khiến' dùng khi ai đó làm điều gì đó mà chính họ cũng không hiểu tại sao, như bị thế lực vô hình thúc đẩy. Đây là cách nói dân gian, không phải hiện tượng ma quỷ thật.",
    },
    {
        "q": "Loại ma nào thường được nhắc trong câu 'ma gà'?",
        "options": ["Gà chết thành ma", "Người chết vì gà", "Quỷ gà", "Thần gà"],
        "correct": 0,
        "explanation": "'Ma gà' là cách gọi dân gian chỉ con gà chết không được chôn cất đàng hoàng, được tin là sẽ thành ma quấy nhiễu. Ngoài ra còn có thành ngữ 'ma gà' chỉ người nhút nhát.",
    },
