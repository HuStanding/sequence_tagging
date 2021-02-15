glove:
	wget -P ./data/ https://apache-mxnet.s3.cn-north-1.amazonaws.com.cn/gluon/embeddings/glove/glove.6B.zip 
	unzip ./data/glove.6B.zip -d data/glove.6B/
	rm ./data/glove.6B.zip
	python model/convert_conll.py

run:
	python build_data.py
	python train.py
	python evaluate.py
