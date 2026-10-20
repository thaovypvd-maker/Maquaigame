import random
import streamlit as st

st.set_page_config(
    page_title="Âm Binh Ký",
    page_icon="👻",
    layout="centered",
    initial_sidebar_state="collapsed",
)

BG_URL = "https://raw.githubusercontent.com/thaovypvd-maker/Maquaigame/80969180e42358d1ec24d4ae8fd4612de5b3a02c/Background%20.JPG"

QUESTIONS = [
    {"q": "Loại ma nào là người bị hổ cắn trong văn hóa dân gian?", "options": ["Ma trành", "Ma da", "Quỷ đói", "Hổ tinh"], "correct": 0, "explanation": "Ma trành là linh hồn của người bị hổ ăn thịt. Người này không thể siêu thoát mà trở thành nô lệ cho con hổ, đi dụ dỗ thêm người khác cho hổ bắt ăn."},
    {"q": "Những linh hồn mất ở sông hồ được dân gian tin là sẽ thành ma gì?", "options": ["Ma lon", "Ma đuối", "Ma da", "Giao Long"], "correct": 2, "explanation": "Ma da là linh hồn của những người chết đuối, thường ẩn nấp ở sông, ao, hồ. Dân gian quan niệm ma da hay kéo chân người bơi lội để bắt thế mạng nhằm tìm cách siêu thoát."},
    {"q": "Một loài quỷ có nguồn gốc từ Phật Giáo của Ấn Độ, đóng vai trò canh giữ, bảo vệ chùa chiền là?", "options": ["Quỷ đói", "Quỷ đầu cẩu", "Quỷ vương", "Quỷ dạ xoa - Yaksha"], "correct": 3, "explanation": "Quỷ Dạ Xoa là một chủng loại linh thể hoặc quỷ thần có nguồn gốc từ thần thoại Ấn Độ cổ đại, sau này được du nhập và tiếp biến trong văn hóa Phật giáo, Bà-la-môn giáo và dân gian Á Đông."},
    {"q": "Một yêu quái là một cây chiên đàn cổ thụ, ngàn năm thành yêu quái đó là?", "options": ["Hồ ly tinh", "Mộc tinh - quỷ xương cuồng", "Tinh tinh", "Xà tinh"], "correct": 1, "explanation": "Mộc tinh hay còn gọi là quỷ xương cuồng là một yêu quái nổi tiếng trong truyền thuyết và thần thoại dân gian Việt Nam từ thời thượng cổ, thời đại Kinh Dương Vương đến thời Đinh Tiên Hoàng."},
    {"q": "Chó trắng mũi đỏ trong dân gian thường được gắn với hình ảnh là?", "options": ["Chó đội nón mê", "Quỷ đầu cẩu", "Cẩu huyết", "Tất cả đáp án trên"], "correct": 0, "explanation": "Chó đội nón mê là một sinh vật hoặc điềm gở mang tính truyền thuyết và tín ngưỡng dân gian lâu đời tại Việt Nam, đặc biệt là vùng đồng quê Bắc Bộ."},
    {"q": "Loại ma được thờ cúng trong nhà để bảo vệ, canh giữ điền trạch là?", "options": ["Ma trơi", "Ma lai", "Ma xó", "Ma men"], "correct": 2, "explanation": "Ma xó là một loại linh hồn hoặc vong linh được nuôi dưỡng và thờ cúng trong nhà để canh giữ, bảo vệ gia trạch hoặc phục vụ cho mục đích riêng của chủ nhân."},
    {"q": "Loại ma có hình dạng là một đám lửa xanh?", "options": ["Ma giấu", "Ma đói - ngạ quỷ", "Thần trùng", "Ma trơi"], "correct": 3, "explanation": "Ma trơi là hiện tượng các đốm lửa nhỏ, lập lòe màu xanh nhạt, trắng, đỏ hoặc vàng thường xuất hiện vào ban đêm ở các khu vực như nghĩa trang, bãi tha ma hay đầm lầy."},
    {"q": "Một dạng quỷ hút máu trong văn hóa tín ngưỡng Tây Bắc là?", "options": ["Ma cà rồng", "Ma cà chua", "Ma cà tím", "Phí phông"], "correct": 3, "explanation": "Trong thế giới quan của người Thái, Phí Phông được xem là một dạng quỷ hút máu hoặc kết hợp giữa xác người và hồn ma."},
    {"q": "Loài thủy quái có hình dạng giống rồng trong dân gian là?", "options": ["Thuồng luồng", "Long vương", "Lông bông", "Ma da"], "correct": 0, "explanation": "Thuồng luồng là một loài thủy quái huyền thoại trong văn hóa dân gian Việt Nam và Á Đông. Được mô tả là hung dữ, có sức mạnh lớn, thường lật úp ghe thuyền hoặc bắt người hại dân vùng sông nước."},
    {"q": "Một loại ma hay được dùng để chửi người khác?", "options": ["Ma lai", "Ma gà", "Âm binh", "Quỷ nhập tràng"], "correct": 2, "explanation": "Âm binh thường bao gồm các vong hồn chưa siêu thoát, oan hồn, linh hồn binh lính tử trận, hoặc các cô hồn vất vưởng được các thầy phù thủy, pháp sư, thầy cúng chiêu mộ và sai khiến."},
    {"q": "Người chết do tai nạn bất đắc kỳ tử, chưa đến tuổi chết, dân gian gọi là gì?", "options": ["Ma trơi", "Ma lai", "Vong chưa siêu thoát", "Ma xó"], "correct": 2, "explanation": "Những người chết đột ngột, chưa hết tuổi thọ thường được tin là vong hồn còn vất vưởng, chưa thể siêu thoát, phải chờ ngày mãn tang hoặc được cúng bái mới đi đầu thai."},
    {"q": "Người chết vào giờ trùng tang được dân gian tin là sẽ thành loại ma gì?", "options": ["Ma trùng", "Ma lai", "Quỷ đói", "Ma gà"], "correct": 0, "explanation": "Trùng tang là hiện tượng người chết vào giờ xấu, được cho là sẽ kéo theo người thân trong gia đình cùng chết. Dân gian thường làm lễ trấn trùng tang để hóa giải."},
    {"q": "Người chết mà mắt vẫn mở, dân gian tin là điều gì?", "options": ["Chết không nhắm mắt vì còn vướng bận", "Sẽ thành ma trơi", "Sẽ hóa thành hổ", "Đã thành thần"], "correct": 0, "explanation": "Quan niệm dân gian cho rằng người chết mà mắt không nhắm là còn vướng bận chuyện trần gian, chưa yên lòng ra đi. Thường người ta vuốt mắt cho người chết để họ được siêu thoát."},
    {"q": "Loại ma thường được miêu tả xuất hiện trong những ngôi nhà hoang, bỏ trống lâu năm?", "options": ["Ma lai", "Ma xó", "Quỷ nhập tràng", "Ma trơi"], "correct": 0, "explanation": "Ma lai là một loại ma dữ, thường được cho là xuất hiện ở những nơi hoang vắng, nhà bỏ trống lâu năm, quấy nhiễu người đi đường hoặc người ngủ qua đêm."},
    {"q": "Loại ma được cho là trú ngụ ở góc nhà, gầm giường, nơi tối tăm?", "options": ["Ma xó", "Ma trơi", "Ma da", "Ma trành"], "correct": 0, "explanation": "Người xưa tin rằng góc nhà, gầm giường là nơi ma xó trú ngụ. Vì vậy nhiều gia đình kiêng kỵ không ngồi lên góc giường, không quét nhà ban đêm vì sợ đuổi ma xó đi."},
    {"q": "Con mèo đen trong dân gian thường được gắn với điềm gì?", "options": ["Điềm lành", "Điềm gở, ma quỷ", "Thần tài", "Sự giàu sang"], "correct": 1, "explanation": "Mèo đen trong quan niệm dân gian nhiều nơi bị coi là điềm gở, gắn với ma quỷ và bóng tối. Tuy nhiên, ở một số nền văn hóa khác, mèo đen lại là biểu tượng may mắn."},
    {"q": "Tiếng chó sủa ban đêm không rõ hướng, dân gian tin là gì?", "options": ["Chó nhìn thấy ma", "Trời sắp mưa", "Có trộm", "Điềm lành"], "correct": 0, "explanation": "Dân gian quan niệm chó có khả năng nhìn thấy những thứ mà mắt người không thấy được, nên khi chó sủa vô cớ ban đêm, người ta tin rằng có ma quỷ hoặc vong hồn đang đi ngang qua."},
    {"q": "Con rắn hổ mang chúa thường gắn với điển tích nào trong dân gian?", "options": ["Rắn thần báo oán", "Thần tài", "Thần nông", "Thổ địa"], "correct": 0, "explanation": "Nhiều điển tích dân gian kể về rắn thần, rắn hổ mang chúa hiện về báo oán hoặc trả thù những người đã từng hại rắn. Đây là biểu tượng của oan hồn không siêu thoát."},
    {"q": "Hiện tượng ma trơi thực chất được khoa học lý giải là do khí gì bốc lên?", "options": ["Oxy", "Photpho hidro (PH3)", "Cacbon dioxit", "Nito"], "correct": 1, "explanation": "Ma trơi thực chất là khí photpho hidro (PH3) và điphotpho tetrahydrua (P2H4) bốc lên từ các chất hữu cơ phân hủy ở nghĩa trang, đầm lầy, gặp oxy trong không khí thì tự cháy, phát sáng xanh."},
    {"q": "Ánh sáng ma quái xuất hiện gần nghĩa trang, bãi tha ma thường gọi là gì?", "options": ["Ma trơi", "Cầu vồng đêm", "Sương mù", "Hào quang"], "correct": 0, "explanation": "Dân gian gọi ánh sáng lập lòe ở nghĩa trang là ma trơi. Người xưa tin đó là linh hồn người chết hiện về, còn khoa học giải thích là hiện tượng hóa học của khí photpho."},
    {"q": "Hiện tượng sương mù dày đặc ở vùng núi được dân gian gắn với loại ma nào?", "options": ["Ma sương", "Ma lai", "Ma trơi", "Ma xó"], "correct": 0, "explanation": "Sương mù dày đặc ở vùng núi thường được dân gian gọi là ma sương — người đi rừng tin rằng sương mù có thể làm lạc đường, mất phương hướng như bị ma che mắt."},
    {"q": "Tiếng gió hú ban đêm được dân gian gọi là gì?", "options": ["Tiếng ma gào", "Tiếng cú kêu", "Tiếng sói hú", "Tiếng thần linh"], "correct": 0, "explanation": "Tiếng gió hú qua khe cửa, hang đá, rừng cây ban đêm thường được dân gian gọi là ma gào hoặc tiếng quỷ khóc. Thực chất đó chỉ là hiện tượng cộng hưởng âm thanh tự nhiên."},
    {"q": "Ma da thường được dân gian miêu tả có đặc điểm gì?", "options": ["Da xanh, tóc dài, ngồi bờ sông", "Đầu trâu mặt ngựa", "Mình người đầu hổ", "Chỉ có một mắt"], "correct": 0, "explanation": "Ma da thường được miêu tả là người phụ nữ da xanh, tóc dài, ngồi bờ sông kéo chân người bơi. Đây là hiện thân của những người chết đuối không siêu thoát."},
    {"q": "Ở Nam Bộ, loại ma nào thường được cho là xuất hiện ở rừng tràm, đầm lầy?", "options": ["Ma trơi", "Ma da", "Ma rừng", "Ma xó"], "correct": 2, "explanation": "Ma rừng là cách gọi dân gian ở Nam Bộ chỉ những linh hồn vất vưởng ở rừng tràm, đầm lầy. Người đi rừng thường kiêng gọi tên, kiêng nói to để không động đến ma rừng."},
    {"q": "Con giao long trong truyền thuyết dân gian thực chất là loài gì?", "options": ["Cá sấu", "Rắn nước lớn", "Rồng thật", "Cá chép hóa rồng"], "correct": 1, "explanation": "Giao long là tên gọi dân gian chỉ loài rắn nước lớn, hoặc cá sấu, được thần thoại hóa thành rồng. Truyền thuyết Lạc Long Quân - Âu Cơ có nhắc đến giao long."},
    {"q": "Quỷ xương cuồng được truyền thuyết mô tả có hình dạng như thế nào?", "options": ["Một đám xương trắng biết đi", "Một con rồng đen", "Một cô gái tóc dài", "Một ông già râu trắng"], "correct": 0, "explanation": "Quỷ xương cuồng được mô tả là một đám xương trắng biết đi, không đầu, không chân, thường xuất hiện ở nơi rừng núi hoang vu. Truyền thuyết kể nó bị diệt bởi các vị thần thời Hùng Vương."},
    {"q": "Hồ ly tinh trong dân gian Việt Nam thường được mô tả là con vật gì hóa thành?", "options": ["Cáo", "Mèo", "Chó", "Rắn"], "correct": 0, "explanation": "Hồ ly tinh là cáo già tu luyện lâu năm hóa thành người, thường là người phụ nữ đẹp quyến rũ đàn ông để hút sinh khí. Truyền thuyết hồ ly tinh phổ biến ở cả Việt Nam và Trung Quốc."},
    {"q": "Con thần trùng trong dân gian là loại ma gì?", "options": ["Ma báo oán", "Ma trơi", "Quỷ dữ", "Thần hộ mệnh"], "correct": 0, "explanation": "Thần trùng là một loại ma báo oán trong tín ngưỡng dân gian, thường được cho là oan hồn của người chết oan ức, tìm cách trả thù người đã hại mình."},
    {"q": "Loài tinh tinh trong dân gian là gì?", "options": ["Một loài yêu tinh", "Con khỉ", "Con vượn", "Con dơi"], "correct": 0, "explanation": "Tinh tinh là cách gọi dân gian chỉ một loại yêu tinh hoặc con vật đã tu luyện thành tinh, thường xuất hiện trong các câu chuyện cổ tích, truyền thuyết."},
    {"q": "Xà tinh trong dân gian là loài gì hóa thành?", "options": ["Rắn", "Rùa", "Cá", "Chim"], "correct": 0, "explanation": "Xà tinh là rắn già tu luyện lâu năm hóa thành yêu tinh, có thể biến thành người. Truyền thuyết xà tinh phổ biến ở nhiều nền văn hóa Á Đông, trong đó có Việt Nam."},
    {"q": "Con thuồng luồng trong dân gian có đặc điểm gì đặc biệt?", "options": ["Có mào đỏ trên đầu", "Có sừng", "Có cánh", "Có hai đuôi"], "correct": 0, "explanation": "Thuồng luồng được miêu tả có mào đỏ trên đầu, thân hình rắn lớn, sống ở sông hồ, có thể lật thuyền và hại người. Đây là loài thủy quái đáng sợ trong tâm thức dân gian."},
    {"q": "Quỷ đói trong quan niệm dân gian là những linh hồn như thế nào?", "options": ["Người chết vì đói", "Người chết vì bệnh", "Người chết vì tai nạn", "Người chết vì chiến tranh"], "correct": 0, "explanation": "Quỷ đói (ngạ quỷ) là những linh hồn người chết vì đói khát, hoặc do tham lam, không biết chia sẻ khi còn sống. Chúng không thể ăn uống, cổ họng nhỏ như kim, miệng phun lửa."},
    {"q": "Lễ cúng cô hồn trong dân gian thường được tổ chức vào ngày nào âm lịch?", "options": ["Rằm tháng 7", "Mùng 1 Tết", "Rằm tháng Giêng", "Ngày 23 tháng Chạp"], "correct": 0, "explanation": "Rằm tháng 7 âm lịch là ngày xá tội vong nhân, dân gian làm lễ cúng cô hồn để bố thí cho những linh hồn không nơi nương tựa, không người thờ cúng."},
    {"q": "Người ta thường cúng gì cho quỷ đói trong dân gian?", "options": ["Cháo trắng, muối gạo", "Thịt mặn", "Bánh chưng", "Trái cây"], "correct": 0, "explanation": "Cháo trắng và muối gạo là lễ vật dân gian dùng để cúng cô hồn, quỷ đói. Cháo loãng tượng trưng cho việc dễ tiêu hóa với cổ họng nhỏ của ngạ quỷ, muối gạo để xua tà khí."},
    {"q": "Theo Phật giáo, quỷ đói (ngạ quỷ) thuộc cõi nào?", "options": ["Cõi ngạ quỷ", "Cõi người", "Cõi trời", "Cõi súc sinh"], "correct": 0, "explanation": "Trong Phật giáo, ngạ quỷ là một trong ba cõi ác (địa ngục, ngạ quỷ, súc sinh). Chúng sinh ở cõi này luôn đói khát nhưng không thể ăn uống, do nghiệp tham lam keo kiệt khi còn sống."},
    {"q": "Quỷ Dạ Xoa thường được tạc tượng ở đâu trong chùa?", "options": ["Cổng chùa, hai bên bậc thềm", "Trong chính điện", "Trên mái chùa", "Dưới gốc cây"], "correct": 0, "explanation": "Tượng quỷ Dạ Xoa thường được tạc ở cổng chùa, hai bên bậc thềm với vẻ mặt dữ tợn để canh giữ, xua đuổi tà ma, bảo vệ không gian linh thiêng của chùa."},
    {"q": "Quỷ La Sát trong Phật giáo có nguồn gốc từ đâu?", "options": ["Ấn Độ", "Trung Quốc", "Nhật Bản", "Việt Nam"], "correct": 0, "explanation": "Quỷ La Sát (Rakshasa) có nguồn gốc từ thần thoại Ấn Độ, sau du nhập vào Phật giáo. Chúng được mô tả là những ác quỷ hung dữ, thường xuất hiện trong kinh điển Phật giáo."},
    {"q": "Quỷ đầu trâu mặt ngựa trong tín ngưỡng dân gian làm nhiệm vụ gì?", "options": ["Dẫn hồn người chết xuống âm phủ", "Canh giữ cổng chùa", "Bảo vệ nhà cửa", "Mang tài lộc đến"], "correct": 0, "explanation": "Đầu trâu (Ngưu Đầu) và mặt ngựa (Mã Diện) là hai quỷ sai dưới quyền Diêm Vương, có nhiệm vụ dẫn hồn người chết xuống âm phủ, thường được thờ trong các đền thờ âm phủ."},
    {"q": "Người ta thường thắp hương vào giờ nào trong ngày để cúng ma quỷ?", "options": ["Giờ Dậu (17-19h)", "Giờ Tý (23-1h)", "Giờ Ngọ (11-13h)", "Giờ Mão (5-7h)"], "correct": 0, "explanation": "Dân gian thường cúng cô hồn, ma quỷ vào buổi chiều tối (giờ Dậu) vì tin rằng đó là lúc âm khí bắt đầu mạnh lên. Cúng ban ngày thường dành cho thần linh, tổ tiên."},
    {"q": "Bàn thờ ông Địa trong nhà có vai trò gì?", "options": ["Cai quản đất đai, nhà cửa", "Cai quản bếp núc", "Cai quản tài lộc", "Cai quản giấc ngủ"], "correct": 0, "explanation": "Ông Địa (Thổ Công) là vị thần cai quản đất đai, nhà cửa, đất ở. Dân gian tin rằng ông Địa trấn giữ, xua đuổi tà ma, bảo vệ bình yên cho gia đình."},
    {"q": "Lễ cúng đất khi làm nhà mới nhằm mục đích gì?", "options": ["Xin phép thần linh, đuổi tà ma", "Cầu tài lộc", "Cầu sức khỏe", "Cầu duyên"], "correct": 0, "explanation": "Cúng đất khi làm nhà là nghi lễ xin phép thần linh, thổ địa và đuổi tà ma khỏi khu đất, đảm bảo gia đình sống yên ổn, không bị quấy nhiễu."},
    {"q": "Người ta thường treo gương trong nhà để làm gì theo tín ngưỡng dân gian?", "options": ["Xua đuổi tà ma", "Trang trí", "Soi gương", "Cầu may"], "correct": 0, "explanation": "Gương được dân gian tin là có khả năng phản chiếu, xua đuổi tà ma, quỷ dữ. Nhiều gia đình treo gương bát quái trước cửa nhà để trấn yểm."},
    {"q": "Bùa chú trong dân gian thường được làm từ chất liệu gì?", "options": ["Giấy vàng, vải đỏ", "Gỗ đào", "Đá núi", "Kim loại quý"], "correct": 0, "explanation": "Bùa chú dân gian thường được vẽ trên giấy vàng, vải đỏ, hoặc khắc lên gỗ đào. Mỗi loại có công dụng riêng: giấy vàng trấn tà, gỗ đào trừ ma, vải đỏ cầu may."},
    {"q": "Cây đào trong dân gian có tác dụng gì theo tín ngưỡng?", "options": ["Trừ tà ma", "Cầu tài lộc", "Cầu duyên", "Chữa bệnh"], "correct": 0, "explanation": "Cây đào được dân gian tin là có khả năng trừ tà ma, xua đuổi điều xấu. Vào dịp Tết, người ta thường cắm cành đào trong nhà để xua đuổi tà khí năm cũ."},
    {"q": "Muối trong tín ngưỡng dân gian có tác dụng gì?", "options": ["Xua đuổi tà ma", "Cầu tài lộc", "Chữa bệnh", "Làm đẹp"], "correct": 0, "explanation": "Muối được dân gian tin là có khả năng thanh tẩy, xua đuổi tà ma. Nhiều người rắc muối quanh nhà, hoặc bỏ muối vào túi áo khi đi đêm để tránh ma quỷ."},
    {"q": "Loại ma nào thường được nhắc đến trong câu ma men?", "options": ["Người nghiện rượu", "Quỷ rượu", "Thần rượu", "Ma trơi"], "correct": 0, "explanation": "Ma men là cách nói dân gian chỉ những người nghiện rượu, uống rượu say không kiểm soát. Từ ma ở đây mang nghĩa ẩn dụ, không phải ma quỷ thật."},
    {"q": "Câu ma cũ bắt nạt ma mới thường dùng để chỉ điều gì?", "options": ["Người mới bị bắt nạt", "Ma quỷ cãi nhau", "Người cũ ghen tị", "Sự may mắn"], "correct": 0, "explanation": "Thành ngữ ma cũ bắt nạt ma mới dùng để chỉ hiện tượng người mới đến thường bị người cũ bắt nạt, ức hiếp. Ma ở đây là cách nói ẩn dụ, không phải ma quỷ thật."},
    {"q": "Người ta thường nói ma xui quỷ khiến khi nào?", "options": ["Khi làm điều gì đó không kiểm soát", "Khi gặp may mắn", "Khi gặp ma thật", "Khi đi chùa"], "correct": 0, "explanation": "Câu ma xui quỷ khiến dùng khi ai đó làm điều gì đó mà chính họ cũng không hiểu tại sao, như bị thế lực vô hình thúc đẩy. Đây là cách nói dân gian, không phải hiện tượng ma quỷ thật."},
    {"q": "Loại ma nào thường được nhắc trong câu ma gà?", "options": ["Gà chết thành ma", "Người chết vì gà", "Quỷ gà", "Thần gà"], "correct": 0, "explanation": "Ma gà là cách gọi dân gian chỉ con gà chết không được chôn cất đàng hoàng, được tin là sẽ thành ma quấy nhiễu. Ngoài ra còn có thành ngữ ma gà chỉ người nhút nhát."},
    {"q": "Địa điểm nào thường được dân gian tin là có nhiều ma quỷ?", "options": ["Nghĩa trang, bãi tha ma", "Chợ đông người", "Trường học", "Bệnh viện"], "correct": 0, "explanation": "Nghĩa trang, bãi tha ma là nơi chôn cất người chết, được dân gian tin là nơi tập trung nhiều linh hồn, ma quỷ. Người ta thường kiêng đi đêm qua nghĩa trang."},
    {"q": "Điều gì được dân gian tin là sẽ xảy ra nếu đi qua nghĩa trang ban đêm?", "options": ["Bị ma trêu, ma nhập", "Gặp may mắn", "Được thần linh phù hộ", "Trở nên giàu có"], "correct": 0, "explanation": "Dân gian tin rằng đi qua nghĩa trang ban đêm có thể bị ma trêu, ma nhập, hoặc gặp điềm gở. Vì vậy nhiều người kiêng đi đêm qua nghĩa trang, đặc biệt là trẻ em và phụ nữ."},
    {"q": "Tại sao người ta thường thắp nhang trong nhà vào buổi tối?", "options": ["Để xua đuổi tà ma, cầu bình an", "Để trang trí", "Để xua muỗi", "Để cầu mưa"], "correct": 0, "explanation": "Thắp nhang buổi tối trong nhà là phong tục dân gian nhằm xua đuổi tà ma, cầu bình an cho gia đình. Khói nhang được tin là có thể thanh tẩy không gian, xua tan âm khí."},
    {"q": "Điều gì được dân gian tin là sẽ xảy ra nếu ai đó gọi tên ma quỷ ban đêm?", "options": ["Ma quỷ sẽ hiện về", "Được may mắn", "Được thần linh phù hộ", "Không có gì xảy ra"], "correct": 0, "explanation": "Dân gian tin rằng gọi tên ma quỷ ban đêm sẽ khiến chúng hiện về, quấy nhiễu. Vì vậy người ta thường kiêng gọi tên các loài ma quỷ, đặc biệt là vào ban đêm."},
    {"q": "Điều gì được dân gian tin là sẽ xảy ra nếu ai đó huýt sáo ban đêm?", "options": ["Ma quỷ sẽ nghe thấy và đến", "Trời sẽ mưa", "Được may mắn", "Không có gì xảy ra"], "correct": 0, "explanation": "Dân gian tin rằng huýt sáo ban đêm sẽ thu hút ma quỷ, vì tiếng sáo được cho là giống tiếng gọi của ma. Vì vậy nhiều người kiêng huýt sáo khi trời tối."},
    {"q": "Vì sao người ta thường kiêng quét nhà vào ban đêm theo tín ngưỡng dân gian?", "options": ["Sợ quét trúng ma xó, đuổi thần tài", "Sợ bụi bay vào mắt", "Sợ ồn ào", "Sợ mất đồ"], "correct": 0, "explanation": "Dân gian kiêng quét nhà ban đêm vì sợ quét trúng ma xó (linh hồn trú ngụ ở góc nhà), hoặc đuổi thần tài, gây mất lộc. Đây là tín ngưỡng dân gian lâu đời."},
    {"q": "Điều gì được dân gian tin là sẽ xảy ra nếu ai đó soi gương lúc nửa đêm?", "options": ["Nhìn thấy ma", "Được may mắn", "Da sẽ đẹp hơn", "Không có gì xảy ra"], "correct": 0, "explanation": "Dân gian tin rằng soi gương lúc nửa đêm có thể nhìn thấy ma, hoặc bị ma nhập vào gương. Vì vậy nhiều người kiêng soi gương vào ban đêm, đặc biệt là giờ Tý."},
    {"q": "Điều gì được dân gian tin là sẽ xảy ra nếu ai đó cắt tóc vào ban đêm?", "options": ["Bị ma cắt tóc, gặp điềm gở", "Tóc mọc nhanh hơn", "Được may mắn", "Không có gì xảy ra"], "correct": 0, "explanation": "Dân gian tin rằng cắt tóc ban đêm có thể bị ma cắt tóc, hoặc gặp điềm gở. Vì vậy nhiều người kiêng cắt tóc vào buổi tối, đặc biệt là trẻ em."},
    {"q": "Điều gì được dân gian tin là sẽ xảy ra nếu ai đó để dao kéo dưới gối khi ngủ?", "options": ["Ma quỷ sẽ không dám đến gần", "Sẽ gặp ác mộng", "Sẽ bị thương", "Không có gì xảy ra"], "correct": 0, "explanation": "Dân gian tin rằng để dao kéo dưới gối khi ngủ sẽ giúp xua đuổi ma quỷ, vì kim loại sắc bén được cho là có khả năng trừ tà. Đây là biện pháp phòng thân dân gian."},
    {"q": "Điều gì được dân gian tin là sẽ xảy ra nếu ai đó ngủ ở nhà hoang?", "options": ["Bị ma quấy nhiễu, ma nhập", "Ngủ ngon hơn", "Được may mắn", "Không có gì xảy ra"], "correct": 0, "explanation": "Dân gian tin rằng ngủ ở nhà hoang, nơi bỏ trống lâu năm có thể bị ma quấy nhiễu, ma nhập, hoặc gặp điềm gở. Vì vậy nhiều người kiêng ngủ qua đêm ở nơi hoang vắng."},
    {"q": "Điều gì được dân gian tin là sẽ xảy ra nếu ai đó đi qua đám tang mà không che mặt?", "options": ["Bị ma nhập, gặp điềm gở", "Được may mắn", "Được thần linh phù hộ", "Không có gì xảy ra"], "correct": 0, "explanation": "Dân gian tin rằng đi qua đám tang mà không che mặt có thể bị ma nhập, hoặc gặp điềm gở, vì linh hồn người chết có thể theo về. Vì vậy nhiều người che mặt khi đi qua đám tang."},
    {"q": "Điều gì được dân gian tin là sẽ xảy ra nếu ai đó nhặt tiền rơi ngoài đường?", "options": ["Bị ma theo, gặp điềm gở", "Được may mắn", "Được thần tài phù hộ", "Không có gì xảy ra"], "correct": 0, "explanation": "Dân gian tin rằng tiền rơi ngoài đường có thể là tiền cúng cô hồn, hoặc tiền của người âm, nhặt về sẽ bị ma theo, gặp điềm gở. Vì vậy nhiều người kiêng nhặt tiền rơi."},
    {"q": "Điều gì được dân gian tin là sẽ xảy ra nếu ai đó ăn cơm cúng cô hồn?", "options": ["Bị ma theo, gặp điềm gở", "Được may mắn", "Được no lâu", "Không có gì xảy ra"], "correct": 0, "explanation": "Dân gian tin rằng ăn cơm cúng cô hồn có thể bị ma theo, gặp điềm gở, vì đồ cúng đã được dâng cho linh hồn. Vì vậy nhiều người kiêng ăn đồ cúng cô hồn."},
    {"q": "Điều gì được dân gian tin là sẽ xảy ra nếu ai đó gọi hồn người chết?", "options": ["Linh hồn sẽ hiện về", "Được may mắn", "Được thần linh phù hộ", "Không có gì xảy ra"], "correct": 0, "explanation": "Dân gian tin rằng gọi hồn người chết có thể khiến linh hồn hiện về, quấy nhiễu người sống. Vì vậy nhiều người kiêng gọi hồn, trừ khi có thầy cúng làm lễ."},
    {"q": "Điều gì được dân gian tin là sẽ xảy ra nếu ai đó đốt vàng mã cho người chết?", "options": ["Người chết sẽ nhận được, siêu thoát", "Người chết sẽ trở về", "Người chết sẽ báo oán", "Không có gì xảy ra"], "correct": 0, "explanation": "Dân gian tin rằng đốt vàng mã cho người chết sẽ giúp họ nhận được đồ cúng, siêu thoát, không còn vất vưởng. Đây là phong tục thờ cúng lâu đời của người Việt."},
    {"q": "Điều gì được dân gian tin là sẽ xảy ra nếu ai đó thắp nhang cho ma đói?", "options": ["Ma đói sẽ được no, không quấy nhiễu", "Ma đói sẽ trở về", "Ma đói sẽ báo oán", "Không có gì xảy ra"], "correct": 0, "explanation": "Dân gian tin rằng thắp nhang, cúng đồ ăn cho ma đói sẽ giúp chúng được no, không quấy nhiễu người sống. Đây là phong tục bố thí, thể hiện lòng từ bi."},
    {"q": "Điều gì được dân gian tin là sẽ xảy ra nếu ai đó động vào mồ mả?", "options": ["Bị ma báo oán, gặp điềm gở", "Được may mắn", "Được thần linh phù hộ", "Không có gì xảy ra"], "correct": 0, "explanation": "Dân gian tin rằng động vào mồ mả, đặc biệt là mồ hoang, có thể bị ma báo oán, gặp điềm gở, vì đã xâm phạm nơi an nghỉ của người chết. Vì vậy nhiều người kiêng động vào mồ mả."},
    {"q": "Điều gì được dân gian tin là sẽ xảy ra nếu ai đó gọi tên người chết ban đêm?", "options": ["Linh hồn sẽ hiện về", "Được may mắn", "Được thần linh phù hộ", "Không có gì xảy ra"], "correct": 0, "explanation": "Dân gian tin rằng gọi tên người chết ban đêm có thể khiến linh hồn hiện về, quấy nhiễu người sống. Vì vậy nhiều người kiêng gọi tên người chết, đặc biệt là vào ban đêm."},
    {"q": "Điều gì được dân gian tin là sẽ xảy ra nếu ai đó đi đêm một mình qua rừng?", "options": ["Bị ma rừng quấy nhiễu", "Được may mắn", "Được thần linh phù hộ", "Không có gì xảy ra"], "correct": 0, "explanation": "Dân gian tin rằng đi đêm một mình qua rừng có thể bị ma rừng quấy nhiễu, làm lạc đường, hoặc gặp điềm gở. Vì vậy nhiều người kiêng đi đêm một mình qua rừng."},
    {"q": "Điều gì được dân gian tin là sẽ xảy ra nếu ai đó tắm sông vào ban đêm?", "options": ["Bị ma da kéo chân", "Được may mắn", "Da sẽ đẹp hơn", "Không có gì xảy ra"], "correct": 0, "explanation": "Dân gian tin rằng tắm sông, ao, hồ vào ban đêm có thể bị ma da kéo chân, bắt thế mạng. Vì vậy nhiều người kiêng tắm sông vào ban đêm, đặc biệt là ở nơi vắng vẻ."},
    {"q": "Điều gì được dân gian tin là sẽ xảy ra nếu ai đó cười đùa ầm ĩ ban đêm?", "options": ["Ma quỷ sẽ nghe thấy và đến", "Trời sẽ mưa", "Được may mắn", "Không có gì xảy ra"], "correct": 0, "explanation": "Dân gian tin rằng cười đùa ầm ĩ ban đêm sẽ thu hút ma quỷ, vì tiếng ồn được cho là phá vỡ không gian yên tĩnh của người âm. Vì vậy nhiều người kiêng cười đùa to vào ban đêm."},
    {"q": "Điều gì được dân gian tin là sẽ xảy ra nếu ai đó để dép ngược chiều?", "options": ["Ma quỷ sẽ không dám đến gần", "Sẽ gặp ác mộng", "Sẽ bị mất dép", "Không có gì xảy ra"], "correct": 0, "explanation": "Dân gian tin rằng để dép ngược chiều trước cửa nhà sẽ khiến ma quỷ không dám đến gần, vì chúng sợ bị đuổi theo. Đây là biện pháp trấn tà dân gian đơn giản."},
    {"q": "Điều gì được dân gian tin là sẽ xảy ra nếu ai đó treo gương trước cửa nhà?", "options": ["Xua đuổi tà ma", "Cầu tài lộc", "Cầu duyên", "Chữa bệnh"], "correct": 0, "explanation": "Gương được dân gian tin là có khả năng phản chiếu, xua đuổi tà ma, quỷ dữ. Nhiều gia đình treo gương bát quái trước cửa nhà để trấn yểm, bảo vệ gia đình."},
    {"q": "Điều gì được dân gian tin là sẽ xảy ra nếu ai đó đeo bùa hộ mệnh?", "options": ["Được bảo vệ khỏi tà ma", "Được may mắn", "Được giàu sang", "Không có gì xảy ra"], "correct": 0, "explanation": "Bùa hộ mệnh được dân gian tin là có khả năng bảo vệ người đeo khỏi tà ma, quỷ dữ, tai nạn. Bùa thường được làm từ giấy vàng, vải đỏ, hoặc gỗ đào, có khắc chữ hoặc hình linh thiêng."},
    {"q": "Điều gì được dân gian tin là sẽ xảy ra nếu ai đó cắm cành đào trong nhà ngày Tết?", "options": ["Xua đuổi tà khí năm cũ", "Cầu tài lộc", "Cầu duyên", "Chữa bệnh"], "correct": 0, "explanation": "Cây đào được dân gian tin là có khả năng trừ tà ma, xua đuổi điều xấu. Vào dịp Tết, người ta thường cắm cành đào trong nhà để xua đuổi tà khí năm cũ, đón năm mới bình an."},
    {"q": "Điều gì được dân gian tin là sẽ xảy ra nếu ai đó rắc muối quanh nhà?", "options": ["Xua đuổi tà ma", "Cầu tài lộc", "Cầu duyên", "Chữa bệnh"], "correct": 0, "explanation": "Muối được dân gian tin là có khả năng thanh tẩy, xua đuổi tà ma. Nhiều người rắc muối quanh nhà, hoặc bỏ muối vào túi áo khi đi đêm để tránh ma quỷ."},
    {"q": "Điều gì được dân gian tin là sẽ xảy ra nếu ai đó thờ ma xó trong nhà?", "options": ["Được ma xó bảo vệ, canh giữ nhà", "Bị ma xó quấy nhiễu", "Bị mất lộc", "Không có gì xảy ra"], "correct": 0, "explanation": "Dân gian tin rằng thờ ma xó trong nhà sẽ được ma xó bảo vệ, canh giữ gia trạch, xua đuổi tà ma. Tuy nhiên, ma xó cũng được cho là có thể quấy nhiễu nếu không được thờ cúng đàng hoàng."},
    {"q": "Điều gì được dân gian tin là sẽ xảy ra nếu ai đó cúng cô hồn vào rằm tháng 7?", "options": ["Cô hồn sẽ được no, không quấy nhiễu", "Cô hồn sẽ trở về", "Cô hồn sẽ báo oán", "Không có gì xảy ra"], "correct": 0, "explanation": "Dân gian tin rằng cúng cô hồn vào rằm tháng 7 sẽ giúp các linh hồn không nơi nương tựa được no, không quấy nhiễu người sống. Đây là phong tục bố thí, thể hiện lòng từ bi."},
    {"q": "Điều gì được dân gian tin là sẽ xảy ra nếu ai đó động vào bàn thờ?", "options": ["Bị thần linh, tổ tiên quở trách", "Được may mắn", "Được thần tài phù hộ", "Không có gì xảy ra"], "correct": 0, "explanation": "Dân gian tin rằng động vào bàn thờ, đặc biệt là bàn thờ tổ tiên, có thể bị thần linh, tổ tiên quở trách, gặp điềm gở. Vì vậy nhiều người kiêng động vào bàn thờ, trừ khi làm lễ cúng."},
    {"q": "Điều gì được dân gian tin là sẽ xảy ra nếu ai đó nói xấu người chết?", "options": ["Bị ma báo oán", "Được may mắn", "Được thần linh phù hộ", "Không có gì xảy ra"], "correct": 0, "explanation": "Dân gian tin rằng nói xấu người chết có thể bị ma báo oán, gặp điềm gở, vì đã xúc phạm linh hồn người đã khuất. Vì vậy nhiều người kiêng nói xấu người chết, đặc biệt là trong đám tang."},
]

TITLES = [
    (0, 3, "Pháp sư hệ vật lý", "🔮"),
    (4, 5, "Thầy pháp tập sự", "🧙"),
    (6, 8, "Full sách thánh", "📖"),
    (9, 10, "Trấn giữ tam giới", "🐉"),
]

def get_title(n):
    for lo, hi, name, icon in TITLES:
        if lo <= n <= hi:
            return name, icon
    return TITLES[0][2], TITLES[0][3]

defaults = {
    "started": False,
    "q_idx": 0,
    "lanterns": 0,
    "wrong_attempted": set(),
    "show_wrong": False,
    "show_explanation": False,
    "finished": False,
    "quiz": [],
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

def start_new_game():
    st.session_state.quiz = random.sample(QUESTIONS, 10)
    st.session_state.q_idx = 0
    st.session_state.lanterns = 0
    st.session_state.wrong_attempted = set()
    st.session_state.show_wrong = False
    st.session_state.show_explanation = False
    st.session_state.finished = False
    st.session_state.started = True

CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;600;700;900&family=Playfair+Display:wght@700;900&display=swap');

#MainMenu, footer, header {{ visibility: hidden; }}

.stApp {{
    background-image: linear-gradient(rgba(2,8,20,0.62), rgba(2,8,20,0.82)), url('{BG_URL}');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    font-family: 'Be Vietnam Pro', sans-serif;
    color: #e0f0ff;
}}

h1, h2, h3 {{
    color: #7feaff !important;
    text-shadow: 0 0 10px #00c8ff, 0 0 24px #0088ff, 0 0 48px #0033aa;
    font-family: 'Playfair Display', 'Be Vietnam Pro', serif;
    letter-spacing: 1px;
}}

.main-title {{
    text-align: center;
    font-family: 'Playfair Display', 'Be Vietnam Pro', serif;
    font-size: 2.4rem;
    font-weight: 900;
    color: #9ff0ff;
    text-shadow: 0 0 12px #00d5ff, 0 0 28px #0088ff, 0 0 60px #0033aa;
    margin: 10px 0 6px 0;
    letter-spacing: 3px;
}}
.subtitle {{
    text-align: center;
    color: #7ab8d8;
    font-size: 0.9rem;
    margin-bottom: 22px;
    letter-spacing: 4px;
    text-transform: uppercase;
}}

@keyframes rainbowLED {{
    0%   {{ border-color: #ff2d55; box-shadow: 0 0 14px rgba(255,45,85,0.9), 0 0 32px rgba(255,45,85,0.45), inset 0 0 12px rgba(255,45,85,0.28); }}
    14%  {{ border-color: #ff9500; box-shadow: 0 0 14px rgba(255,149,0,0.9), 0 0 32px rgba(255,149,0,0.45), inset 0 0 12px rgba(255,149,0,0.28); }}
    28%  {{ border-color: #ffea00; box-shadow: 0 0 14px rgba(255,234,0,0.9), 0 0 32px rgba(255,234,0,0.45), inset 0 0 12px rgba(255,234,0,0.28); }}
    42%  {{ border-color: #2dff5c; box-shadow: 0 0 14px rgba(45,255,92,0.9), 0 0 32px rgba(45,255,92,0.45), inset 0 0 12px rgba(45,255,92,0.28); }}
    57%  {{ border-color: #00e5ff; box-shadow: 0 0 14px rgba(0,229,255,0.9), 0 0 32px rgba(0,229,255,0.45), inset 0 0 12px rgba(0,229,255,0.28); }}
    71%  {{ border-color: #2d6bff; box-shadow: 0 0 14px rgba(45,107,255,0.9), 0 0 32px rgba(45,107,255,0.45), inset 0 0 12px rgba(45,107,255,0.28); }}
    85%  {{ border-color: #bb33ff; box-shadow: 0 0 14px rgba(187,51,255,0.9), 0 0 32px rgba(187,51,255,0.45), inset 0 0 12px rgba(187,51,255,0.28); }}
    100% {{ border-color: #ff2d55; box-shadow: 0 0 14px rgba(255,45,85,0.9), 0 0 32px rgba(255,45,85,0.45), inset 0 0 12px rgba(255,45,85,0.28); }}
}}

.intro-box {{
    background: rgba(0, 22, 45, 0.68);
    border: 2px solid #00d5ff;
    border-radius: 14px;
    padding: 26px 28px;
    margin: 20px 0;
    backdrop-filter: blur(6px);
    animation: rainbowLED 5s linear infinite;
    color: #dff6ff;
    line-height: 1.8;
}}
.intro-label {{
    color: #7feaff;
    font-family: 'Playfair Display', serif;
    font-size: 1.3rem;
    font-weight: 900;
    margin-bottom: 16px;
    text-shadow: 0 0 10px rgba(0,213,255,0.7);
    letter-spacing: 3px;
    text-align: center;
}}
.intro-text {{
    font-size: 1.02rem;
    margin-bottom: 14px;
    text-align: justify;
}}
.intro-whisper {{
    color: #ffaa66;
    text-align: center;
    font-style: italic;
    margin-top: 22px;
    font-size: 1rem;
    text-shadow: 0 0 10px rgba(255,170,102,0.5);
    letter-spacing: 1px;
}}

.status-bar {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: rgba(0, 20, 40, 0.55);
    border: 1px solid rgba(0, 213, 255, 0.5);
    border-radius: 12px;
    padding: 10px 18px;
    margin-bottom: 18px;
    box-shadow: 0 0 12px rgba(0, 213, 255, 0.35);
    backdrop-filter: blur(4px);
    font-weight: 600;
    color: #bfe9ff;
}}
.status-bar .lanterns {{
    font-size: 1.1rem;
    letter-spacing: 2px;
    color: #ffd27f;
}}

.question-box {{
    background: rgba(0, 22, 45, 0.62);
    border: 3px solid #00d5ff;
    border-radius: 14px;
    padding: 22px 26px;
    margin-bottom: 20px;
    backdrop-filter: blur(6px);
    animation: rainbowLED 4s linear infinite;
    font-size: 1.18rem;
    font-weight: 700;
    color: #dff6ff;
    text-shadow: 0 0 8px rgba(0, 213, 255, 0.6);
}}

[class*="st-key-opt_"] button {{
    background: rgba(0, 18, 38, 0.72) !important;
    color: #dff6ff !important;
    border: 2px solid #00c8ff !important;
    border-radius: 10px !important;
    padding: 14px 22px !important;
    font-family: 'Be Vietnam Pro', sans-serif !important;
    font-weight: 600 !important;
    font-size: 1.05rem !important;
    width: 100% !important;
    text-align: left !important;
    transition: all 0.18s ease !important;
    animation: rainbowLED 2.5s linear infinite !important;
    margin-bottom: 6px;
}}
[class*="st-key-opt_"] button:hover {{
    background: rgba(0, 60, 110, 0.9) !important;
    color: #ffffff !important;
    transform: translateY(-1px) scale(1.01);
}}

.st-key-start_btn button {{
    background: rgba(70, 40, 0, 0.85) !important;
    border: 2px solid #ffcc55 !important;
    color: #fff4d0 !important;
    box-shadow: 0 0 16px #ffcc55, inset 0 0 12px rgba(255,204,85,0.3) !important;
    animation: goldBlink 1.8s infinite !important;
    text-align: center !important;
    font-size: 1.15rem !important;
    padding: 15px 22px !important;
    margin-top: 16px !important;
}}
.st-key-start_btn button:hover {{
    background: rgba(120, 70, 0, 0.95) !important;
    box-shadow: 0 0 30px #ffe9a0, 0 0 60px rgba(255,233,160,0.7) !important;
}}
@keyframes goldBlink {{
    0%, 100% {{ border-color: #ffcc55; box-shadow: 0 0 12px rgba(255,204,85,0.7), inset 0 0 10px rgba(255,204,85,0.25); }}
    50% {{ border-color: #ffe9a0; box-shadow: 0 0 28px rgba(255,233,160,1), inset 0 0 22px rgba(255,233,160,0.45); }}
}}

.st-key-continue_btn button {{
    background: rgba(0, 60, 30, 0.85) !important;
    border: 2px solid #22ff88 !important;
    color: #d4ffe4 !important;
    box-shadow: 0 0 14px #22ff88, inset 0 0 12px rgba(34,255,136,0.3) !important;
    animation: greenBlink 1.8s infinite !important;
    text-align: center !important;
    font-size: 1.12rem !important;
    padding: 14px 22px !important;
    margin-top: 14px !important;
}}
.st-key-continue_btn button:hover {{
    background: rgba(0, 100, 50, 0.95) !important;
    box-shadow: 0 0 26px #44ffaa, 0 0 52px rgba(68,255,170,0.7) !important;
}}
@keyframes greenBlink {{
    0%, 100% {{ border-color: #22ff88; box-shadow: 0 0 10px rgba(34,255,136,0.6), inset 0 0 10px rgba(34,255,136,0.2); }}
    50% {{ border-color: #88ffcc; box-shadow: 0 0 24px rgba(136,255,204,1), inset 0 0 20px rgba(136,255,204,0.4); }}
}}

.st-key-retry_btn {{
    position: fixed !important;
    bottom: 12% !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
    z-index: 100001 !important;
    width: min(400px, 85vw) !important;
}}
.st-key-retry_btn button {{
    background: rgba(80, 20, 0, 0.92) !important;
    border: 2px solid #ff8833 !important;
    color: #ffe0c8 !important;
    box-shadow: 0 0 16px #ff8833, inset 0 0 12px rgba(255,136,51,0.35) !important;
    animation: orangeBlink 1.2s infinite !important;
    text-align: center !important;
    font-size: 1.1rem !important;
    padding: 14px 22px !important;
}}
.st-key-retry_btn button:hover {{
    background: rgba(140, 40, 0, 0.95) !important;
    box-shadow: 0 0 30px #ffaa55, 0 0 60px rgba(255,170,85,0.7) !important;
}}
@keyframes orangeBlink {{
    0%, 100% {{ border-color: #ff8833; box-shadow: 0 0 12px rgba(255,136,51,0.7), inset 0 0 10px rgba(255,136,51,0.25); }}
    50% {{ border-color: #ffbb66; box-shadow: 0 0 28px rgba(255,187,102,1), inset 0 0 22px rgba(255,187,102,0.45); }}
}}

.st-key-restart_btn button {{
    background: rgba(40, 0, 60, 0.85) !important;
    border: 2px solid #bb66ff !important;
    color: #f0dfff !important;
    box-shadow: 0 0 16px #bb66ff, inset 0 0 12px rgba(187,102,255,0.3) !important;
    text-align: center !important;
    font-size: 1.1rem !important;
    padding: 14px 22px !important;
}}
.st-key-restart_btn button:hover {{
    background: rgba(70, 0, 110, 0.95) !important;
    box-shadow: 0 0 30px #cc88ff, 0 0 60px rgba(204,136,255,0.7) !important;
}}

.explain-box {{
    background: rgba(0, 30, 50, 0.78);
    border: 2px solid #00ffcc;
    border-radius: 14px;
    padding: 22px 26px;
    margin: 18px 0;
    backdrop-filter: blur(6px);
    box-shadow: 0 0 18px #00ffcc, 0 0 40px rgba(0,255,204,0.5), inset 0 0 22px rgba(0,255,204,0.15);
    color: #e0fff8;
    font-size: 1.05rem;
    line-height: 1.7;
}}
.explain-box .correct-ans {{
    color: #7dffcf;
    font-weight: 700;
    text-shadow: 0 0 8px rgba(0,255,180,0.7);
    margin-bottom: 14px;
    font-size: 1.1rem;
}}
.explain-box .label {{
    color: #7feaff;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    font-size: 0.85rem;
    margin-bottom: 6px;
    display: block;
}}
.explain-box .concept {{
    font-size: 1rem;
    color: #d0f0ff;
}}

.wrong-overlay {{
    position: fixed;
    inset: 0;
    background: radial-gradient(circle at center, rgba(220,30,30,0.92), rgba(40,0,0,0.98));
    z-index: 99999;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    animation: redFlash 0.5s ease-out;
    font-family: 'Be Vietnam Pro', sans-serif;
    pointer-events: none;
}}
@keyframes redFlash {{
    0% {{ opacity: 0; }}
    50% {{ opacity: 1; background: radial-gradient(circle at center, rgba(255,80,80,0.95), rgba(80,0,0,1)); }}
    100% {{ opacity: 1; }}
}}
.wrong-text {{
    color: #fff;
    font-size: 3.2rem;
    font-weight: 900;
    letter-spacing: 6px;
    text-shadow: 0 0 20px #ff0000, 0 0 40px #ff3333, 0 0 80px #aa0000;
    margin-bottom: 30px;
    animation: textShake 0.5s infinite;
}}
@keyframes textShake {{
    0%, 100% {{ transform: translateX(0); }}
    25% {{ transform: translateX(-4px); }}
    75% {{ transform: translateX(4px); }}
}}
.ghost-icons {{
    font-size: 7rem;
    display: inline-block;
    opacity: 0;
    animation: descend 2.8s ease-in-out forwards;
    filter: drop-shadow(0 0 24px #ff2222) drop-shadow(0 0 48px #aa0000);
}}
@keyframes descend {{
    0% {{ transform: translateY(-500px); opacity: 0; }}
    20% {{ opacity: 1; }}
    100% {{ transform: translateY(0); opacity: 1; }}
}}
.wrong-hint {{
    color: #ffd0d0;
    font-size: 0.95rem;
    margin-top: 36px;
    letter-spacing: 3px;
    text-transform: uppercase;
    opacity: 0.9;
    text-align: center;
}}

.end-box {{
    background: rgba(0, 20, 40, 0.75);
    border: 3px solid #00d5ff;
    border-radius: 16px;
    padding: 30px 28px;
    text-align: center;
    backdrop-filter: blur(8px);
    animation: rainbowLED 5s linear infinite;
    margin: 20px 0;
}}
.end-label {{
    color: #7ab8d8;
    letter-spacing: 4px;
    font-size: 0.85rem;
    text-transform: uppercase;
    margin-bottom: 8px;
}}
.end-title {{
    color: #9ff0ff;
    font-family: 'Playfair Display', 'Be Vietnam Pro', serif;
    font-size: 2.3rem;
    font-weight: 900;
    text-shadow: 0 0 14px #00d5ff, 0 0 30px #0088ff, 0 0 60px #0033aa;
    letter-spacing: 2px;
    margin-bottom: 8px;
}}
.end-icon {{
    font-size: 4rem;
    margin-bottom: 10px;
}}
.end-lanterns {{
    font-size: 1.5rem;
    color: #ffd27f;
    letter-spacing: 4px;
    margin: 14px 0;
    text-shadow: 0 0 10px rgba(255,180,80,0.7);
}}
.tier-list {{
    margin-top: 22px;
    padding-top: 18px;
    border-top: 1px dashed rgba(0,213,255,0.4);
    font-size: 0.92rem;
    color: #a8c8e0;
    text-align: left;
}}
.tier-list .tier {{
    padding: 6px 0;
    border-bottom: 1px dashed rgba(0,213,255,0.15);
}}
.tier-list .tier.current {{
    color: #9ff0ff;
    font-weight: 700;
    text-shadow: 0 0 8px rgba(0,213,255,0.7);
}}
.re-attempt-note {{
    text-align: center;
    color: #ffaa66;
    margin-top: 12px;
    font-style: italic;
    font-size: 0.92rem;
    text-shadow: 0 0 6px rgba(255,170,102,0.4);
}}

@media (max-width: 640px) {{
    .main-title {{ font-size: 1.5rem; }}
    .wrong-text {{ font-size: 2rem; }}
    .ghost-icons {{ font-size: 5rem; }}
    .end-title {{ font-size: 1.7rem; }}
    .question-box {{ font-size: 1.02rem; padding: 16px 18px; }}
    .status-bar {{ font-size: 0.85rem; }}
    .intro-box {{ padding: 18px 20px; }}
}}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

def lanterns_display(n):
    return "🏮" * n if n > 0 else "—"

def render_status_bar(idx):
    st.markdown(f"""
    <div class="status-bar">
        <div>📜 Câu {idx+1} / 10</div>
        <div class="lanterns">{lanterns_display(st.session_state.lanterns)} ({st.session_state.lanterns})</div>
    </div>
    """, unsafe_allow_html=True)

def render_intro():
    st.markdown("""
    <div class="intro-box">
        <div class="intro-label">📜 · Lời Tựa ·</div>
        <div class="intro-text">
            Giữa cõi âm dương mờ ảo, con người từ ngàn đời vẫn truyền tai nhau những câu chuyện về ma quái —
            những linh hồn không siêu thoát, những yêu tinh ẩn mình trong cây cỏ, sông hồ, và cả trong
            những ngôi nhà tưởng chừng bình yên nhất.
        </div>
        <div class="intro-text">
            <b>Âm Binh Ký</b> là hành trình lật giở <b>10 trang ký sự</b> về các loài ma quỷ trong dân gian Việt Nam.
            Mỗi câu trả lời đúng, ngươi sẽ thắp lên một ngọn đèn 🏮 — soi đường thoát khỏi màn đêm âm khí.
            Nhưng coi chừng: chỉ cần một phen lầm lạc, ma quỷ sẽ hiện về, và cơ hội tích đèn sẽ vụt mất.
        </div>
        <div class="intro-whisper">Ngươi đã sẵn sàng bước vào cõi âm chưa…? 👻</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🕯️   Bắt đầu hành trình", key="start_btn", use_container_width=True):
        start_new_game()
        st.rerun()

def render_question():
    idx = st.session_state.q_idx
    if idx >= len(st.session_state.quiz):
        st.session_state.finished = True
        st.rerun()
    q = st.session_state.quiz[idx]
    render_status_bar(idx)

    st.markdown(f'<div class="question-box">❓ {q["q"]}</div>', unsafe_allow_html=True)

    was_wrong = idx in st.session_state.wrong_attempted

    for i, opt in enumerate(q["options"]):
        label = f"{chr(65+i)}. {opt}"
        if st.button(label, key=f"opt_{idx}_{i}", use_container_width=True):
            if i == q["correct"]:
                if not was_wrong:
                    st.session_state.lanterns += 1
                st.session_state.show_explanation = True
                st.rerun()
            else:
                st.session_state.wrong_attempted.add(idx)
                st.session_state.show_wrong = True
                st.rerun()

    if was_wrong:
        st.markdown('<div class="re-attempt-note">⚠ Bạn đã trả lời sai câu này — lần này không tính điểm 🏮</div>',
                    unsafe_allow_html=True)

def render_wrong():
    st.markdown("""
    <div class="wrong-overlay">
        <div class="wrong-text">SAI RỒI!</div>
        <div class="ghost-icons">👻😡</div>
        <div class="wrong-hint">Ma quỷ đang hiện về...</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("↺  Chọn lại câu trả lời", key="retry_btn", use_container_width=True):
        st.session_state.show_wrong = False
        st.rerun()
    st.stop()

def render_explanation():
    idx = st.session_state.q_idx
    q = st.session_state.quiz[idx]
    correct_letter = chr(65 + q["correct"])
    correct_text = q["options"][q["correct"]]

    render_status_bar(idx)
    st.markdown(f'<div class="question-box">❓ {q["q"]}</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="explain-box">
        <span class="label">✅ Đáp án đúng</span>
        <div class="correct-ans">{correct_letter}. {correct_text}</div>
        <span class="label">📖 Khái niệm</span>
        <div class="concept">{q["explanation"]}</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("➜  Tiếp tục", key="continue_btn", use_container_width=True):
        st.session_state.show_explanation = False
        st.session_state.q_idx += 1
        if st.session_state.q_idx >= len(st.session_state.quiz):
            st.session_state.finished = True
        st.rerun()

def render_end():
    n = st.session_state.lanterns
    title_name, title_icon = get_title(n)

    tiers_html = ""
    for lo, hi, name, icon in TITLES:
        is_current = (lo <= n <= hi)
        cls = "tier current" if is_current else "tier"
        range_text = f"{lo}–{hi}"
        marker = " ◀ BẠN" if is_current else ""
        tiers_html += f'<div class="{cls}">{icon} {range_text} 🏮 → {name}{marker}</div>'

    st.markdown(f"""
    <div class="end-box">
        <div class="end-icon">{title_icon}</div>
        <div class="end-label">Danh hiệu của bạn</div>
        <div class="end-title">{title_name}</div>
        <div class="end-lanterns">{lanterns_display(n)} {n}/10 🏮</div>
        <div class="tier-list">
            <div style="color:#7feaff;font-weight:700;margin-bottom:8px;">🏅 Các danh hiệu khác</div>
            {tiers_html}
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔄  Chơi lại từ đầu", key="restart_btn", use_container_width=True):
        st.session_state.started = False
        st.session_state.finished = False
        st.session_state.quiz = []
        st.rerun()

st.markdown('<div class="main-title">👻 ÂM BINH KÝ 👻</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ký sự trắc nghiệm ma quái dân gian</div>', unsafe_allow_html=True)

if st.session_state.finished:
    render_end()
elif not st.session_state.started:
    render_intro()
elif st.session_state.show_wrong:
    render_wrong()
elif st.session_state.show_explanation:
    render_explanation()
else:
    render_question()
