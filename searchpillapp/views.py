from django.shortcuts import render
import numpy as np
from PIL import Image
import tensorflow.keras as keras
from tensorflow.keras.layers import *
from tensorflow.keras.models import *
from searchpillapp.forms import ProductForm

model_path = 'C:/Users/dltnw/Desktop/bbibbi/BBIBBI/searchpillapp/Pill_image_pretrained_mobile_model_2.h5'
model = keras.models.load_model(model_path)

class_list = ['가네탑에스연질캡슐',
  '가바로닌캡슐100mg',
  '가바틴캡슐300밀리그람',
  '나리센연질캡슐',
  '나이시드캡슐150㎎',
  '나프민캡슐',
  '네오로신캡슐',
  '넥사졸캡슐20밀리그램',
  '넬슨세픽심캡슐',
  '누코미트캡슐200밀리그램',
  '뉴로낙CR정',
  '뉴트로필정',
  '다이뉴에이치알정',
  '다이피릴엠정2',
  '대우세파클러캡슐250밀리그램',
  '독시라마이신캡슐100mg',
  '동인당은행엽엑스정',
  '두타반플러스정',
  '드로본정150밀리그램',
  '디',
  '디젠정',
  '레벡스캡슐',
  '로텐연질캡슐',
  '로페란캡슐',
  '리드덴타캡슐',
  '리드미캡슐',
  '리리베아캡슐75mg',
  '리버플란연질캡슐',
  '린코신캡슐',
  '메바론정',
  '뮤코원캡슐',
  '베아라제정',
  '벤포킹정',
  '보령독시플루리딘캡슐100밀리그램',
  '복합쓸기담연질캡슐',
  '부코펜정',
  '브라덱신캡슐',
  '비스펜틴조절방출캡슐10mg',
  '비타마인연질캡슐',
  '비타코플러스연질캡슐',
  '빅톤연질캡슐',
  '빅파워비타연질캡슐',
  '삼진제테파캅셀',
  '설포린캡슐',
  '세푸르엠정250mg',
  '세프로캅셀',
  '셀막비타연질캡슐',
  '셀벡스캡슐',
  '스파졸캡슐',
  '시세틴20밀리그램캡슐',
  '실로스타엠서방캡슐200밀리그램',
  '실로스탄씨알정200밀리그램',
  '씨베리움캡슐',
  '아노벤캅셀',
  '아세테밍정',
  '아세트라셋정',
  '아웃콜코정',
  '아웃콜코프캡슐',
  '아크랑캅셀',
  '아트렌캡슐50밀리그램',
  '알리코이부프로펜정400mg',
  '알마믹스정',
  '알보젠레날리도마이드캡슐5밀리그램',
  '에니트정10',
  '에도날캡슐',
  '에란탄지속정60밀리그램',
  '에카린에이정',
  '엘도브론캡슐300밀리그램',
  '엠지비타-에프정',
  '엠지비타에프정',
  '오스가바캡슐100밀리그램',
  '옥트산에이치알정',
  '원트란서방정',
  '유로비트에스알캡슐4밀리그람',
  '이연클래리트로마이신정500밀리그램',
  '잘보빈정500밀리그램',
  '제로픽스정1밀리그램',
  '제트-유정',
  '조인사민캡슐',
  '콘서타OROS서방정54밀리그램',
  '콘티푸로스연질캡슐',
  '쿨노즈캡슐',
  '큐리티연질캡슐',
  '타이노즈연질캡슐',
  '타이레놀정500밀리그람',
  '타크로리캡슐0',
  '타크로스캡슐0',
  '탑픽스정1밀리그램',
  '트라마롤세미정',
  '트라마펜정',
  '파미버정',
  '팜슈어정750밀리그램',
  '프로부펜정400밀리그램',
  '프로세틴캡슐20mg',
  '프리린캡슐150밀리그램',
  '프릭딘캡슐10mg',
  '피도글에이캡슐',
  '피엠에스리스페리돈정0',
  '하디디앤엔연질캡슐',
  '하모빅캡슐',
  '헤파라이프연질캡슐350mg',
  '휴온스니자티딘캡슐150mg'
]


def pills(request):
  if request.method == 'POST':
    form = ProductForm(request.POST, request.FILES)
    if form.is_valid():
      image_file = request.FILES.get('imgfile')

      # 이미지 처리 및 예측
      image = Image.open(image_file)
      image = image.resize((224, 224))
      image = np.array(image)
      image = image / 255.
      image = np.reshape(image, (1, 224, 224, 3))

      prediction = model.predict(image)
      pred_class = np.argmax(prediction, axis=-1)
      pred_class_label = class_list[int(pred_class)]

      return render(request, 'searchpillapp/result.html', {'prediction': pred_class_label})

  form = ProductForm()
  return render(request, 'searchpillapp/pills.html', {'form': form})