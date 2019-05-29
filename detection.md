## 检测

####基本知识  
- [ ] 非极大值抑制NMS  
  ```各类分别处理．对于每一类，首先保留置信度最大的框，然后去除与这个框IOU大于一定阀值的框，除了刚刚已经保留的最大置信度的框和已经去除的框，
  继续保留剩余框置信度最大的框，再去除与这个框IOU大于一定阀值的框...以此类推，最后保留的是置信度都比较大并且靠的不是很近的框。
  ```
- [ ] hard negative mining  
  ```负样本很多的时候可以采用，就是说模型训练好之后，拿训练样本去测试，结果产生很多假正样本，再拿这些假正样本当做负样本去继续训练。  
  ```
  
#### One-Stage 
- SSD
- YoLO
#### Two-Stage 
- Faster-RCNN
- FPN

#### 深入理解
- 说一说One-stage和Two-stage两者有什么特点



#### 常见问题
- [ ] faster RCNN 跟fast Rcnn有啥不同
- [ ] SSD细节 SSD怎么改动变成FasterRCNN    
- [ ] RPN的作用  
- [ ] ROI Align的作用    
- [ ] 跟SSD YOLO有啥不同  
- [ ] 解释一下FPN  
- [ ] rcnn到faster rcnn，介绍一下，然后具体每一步操作都问的很细，roi pooling具体怎么做的、RPN是怎么做的，输入输出是什么
- [ ] faster rcnn的最后输出大小是多少、它的正负样本是怎么选择的  
- [ ] nms具体怎么做的，假设这是一个函数，那么这个函数输入输出是什么，中间操作又是怎么做的
- [ ] Focal Loss 原理  
- [ ] One-Stage\Two-Stage  SSD原理  
- [ ] IoUNet的原理  
- [ ] 轻量级的检测器  
- [ ] NMS和soft-NMS原理  
- [ ] SSD和Faster-RCNN，说一下异同点  
- [ ] Faster-RCNN的回归目标是如何定义的  
- [ ] Faster-RCNN用的什么loss, smooth L1 loss为什么更有效 
- [ ] 多尺度训练如何设置  
- [ ] 为什么设置长边为固定的1600  
- [ ] roi align \ roi pooling 
- [ ] RPN哪里也可以提升小目标检出率 
- [ ] 为什么说resnet101不适用于目标检测  
- [ ] 小目标在FPN的什么位置检测 
- [ ] detnet 
- [ ] 手写nms
- [ ] 一个图片中有一个很大的目标还有一个很小的目标
- [ ] 大目标如果有2个候选框和gt重合应该怎么处理  
- [ ] 视觉的attention
- [ ] mobilenet(DepthWise convolution)  
- [ ] Faster RCNN的损失函数  
- [ ] 针对小目标的解决措施
- [ ] 如何解决类内的检测
- [ ] 说一下faster-rcnn的整个从输入到输出的框架流程　　
- [ ] focal loss具体怎么操作的   
- [ ] 如果有很长，很小，或者很宽的目标，应该如何处理
- [ ] FPN的特征融合具体是怎么做的
- [ ] FPN的特征融合为什么是相加操作呢
- [ ] 为什么说resnet101不适用于目标检测
- [ ] 小目标在FPN的什么位置检测  
- [ ] 还知道哪些轻量级的检测器
 
 
 
 
 
 
 

