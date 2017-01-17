all: max-stock

max-stock:
	swagger_py_codegen -s max_stock.yaml . -p app
