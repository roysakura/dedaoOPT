# -*- coding: utf-8 -*-
import sys

def main():
	if len(sys.argv) == 3:
		cur, target = sys.argv[1:]
		
		cur = float(cur)
		target = float(target)
		
		range_6 = range(0,int(target/6)+2)
		range_68 = range(0,int(target/68)+2)
		range_88 = range(0,int(target/88)+2)
		range_208 = range(0,int(target/208)+2)
		range_388 = range(0,int(target/388)+2)
		range_998 = range(0,int(target/998)+2)

		results = {}
		for a in range_6:
			for b in range_68:
				for c in range_88:
					for d in range_208:
						for e in range_388:
							for f in range_998:
								result = 6*a + 68*b + 88*c + 208*d + 388*e + 998*f + cur - target
								if result>=0:
									results[(a,b,c,d,e,f)] = (result)
		sorted_results = sorted(results.items(), key=lambda kv: kv[1])
		coin6,coin68,coin88,coin208,coin388,coin998 = (sorted_results[0][0])
		print()
		print(u'最划算的充值是{}个6元, {}个68元, {}个88元, {}个208元, {}个388元, {}个998元, 将剩余{:.2f}元'.format(coin6,coin68,coin88,coin208,coin388,coin998,(results[sorted_results[0][0]])))
		print()

	else:
		print(u'使用方法:')
		print(u'\t\t\tpython minimum_deposit.py <输入现在账户余额> <输入目标产品价格>')
		print(u'\t\t\t如: python minimum_deposit.py 5.9 199')


if __name__ == '__main__':
    main()