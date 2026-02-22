import os


def create_mission1(stocks):
	mission1 = '' +\
		'mission "gci stock setup"\n' +\
		'	entering\n' +\
		'	invisible\n' +\
		'	destination "Earth"\n' +\
		'	on offer\n' +\
		'		"stock last day" = "days since start"\n' +\
		'%setstockvalue%' +\
		'%setstockamount%' +\
		'		fail\n'
	setstockvalue = ''
	setstockamount = ''
	for i in range(0, len(stocks)):
		splitted = stocks[i].split('|')
		setstockvalue += '		"stock value ' + splitted[0] + '" = ' + splitted[1] + '\n'
		setstockamount += '		"stock amount ' + splitted[0] + '" = 0' + '\n'
	mission1 = mission1.replace('%setstockvalue%', setstockvalue)
	mission1 = mission1.replace('%setstockamount%', setstockamount)
	return mission1


def create_mission2(stocks):
	mission2 = '' +\
		'mission "gci stock dividends"\n' +\
		'	entering\n' +\
		'	invisible\n' +\
		'	repeat\n' +\
		'	non-blocking\n' +\
		'	destination "Earth"\n' +\
		'	to offer\n' +\
		'		or\n' +\
		'			and\n' +\
		'				"day" == 1\n' +\
		'				"month" == 1\n' +\
		'			and\n' +\
		'				"day" == 1\n' +\
		'				"month" == 4\n' +\
		'			and\n' +\
		'				"day" == 1\n' +\
		'				"month" == 7\n' +\
		'			and\n' +\
		'				"day" == 1\n' +\
		'				"month" == 10\n' +\
		'%tooffer%' +\
		'	on offer\n' +\
		'		conversation\n' +\
		'			label "start"\n' +\
		'			action\n' +\
		'				"passed days" = "days since start" - "stock last day"\n' +\
		'			``\n' +\
		'			label "days loop"\n' +\
		'			branch "end"\n' +\
		'				"passed days" == 0\n' +\
		'			action\n' +\
		'%tendencyroll%' +\
		'%stocktemplates%' +\
		'			action\n' +\
		'				"passed days" -= 1\n' +\
		'			branch "days loop"\n' +\
		'			label "end"\n' +\
		'			action\n' +\
		'				"stock last day" = "days since start"\n' +\
		'%dividends%' +\
		'%dividendsaddi%' +\
		'				"stock all dividends" = "stock dividends addi"\n' +\
		'\n' +\
		'			label "dividends payment 100k"\n' +\
		'			branch "dividends payment 10k"\n' +\
		'				"stock dividends addi" < 100000\n' +\
		'			action\n' +\
		'				payment 100000\n' +\
		'				"stock dividends addi" -= 100000\n' +\
		'			branch "dividends payment 100k"\n' +\
		'\n' +\
		'			label "dividends payment 10k"\n' +\
		'			branch "dividends payment 1k"\n' +\
		'				"stock dividends addi" < 10000\n' +\
		'			action\n' +\
		'				payment 10000\n' +\
		'				"stock dividends addi" -= 10000\n' +\
		'			branch "dividends payment 10k"\n' +\
		'\n' +\
		'			label "dividends payment 1k"\n' +\
		'			branch "dividends payment 100"\n' +\
		'				"stock dividends addi" < 1000\n' +\
		'			action\n' +\
		'				payment 1000\n' +\
		'				"stock dividends addi" -= 1000\n' +\
		'			branch "dividends payment 1k"\n' +\
		'\n' +\
		'			label "dividends payment 100"\n' +\
		'			branch "dividends payment 10"\n' +\
		'				"stock dividends addi" < 100\n' +\
		'			action\n' +\
		'				payment 100\n' +\
		'				"stock dividends addi" -= 100\n' +\
		'			branch "dividends payment 100"\n' +\
		'\n' +\
		'			label "dividends payment 10"\n' +\
		'			branch "dividends payment 1"\n' +\
		'				"stock dividends addi" < 10\n' +\
		'			action\n' +\
		'				payment 10\n' +\
		'				"stock dividends addi" -= 10\n' +\
		'			branch "dividends payment 10"\n' +\
		'\n' +\
		'			label "dividends payment 1"\n' +\
		'			branch "dividends payment done"\n' +\
		'				"stock dividends addi" < 1\n' +\
		'			action\n' +\
		'				payment 1\n' +\
		'				"stock dividends addi" -= 1\n' +\
		'			branch "dividends payment 1"\n' +\
		'\n' +\
		'			label "dividends payment done"\n' +\
		'			scene "scene/stock_chart_analysis"\n' +\
		'			`This is your quarterly stock report and divident payout.`\n' +\
		'%overview%' +\
		'			``\n' +\
		'			`All dividend payouts: &[stock all dividends]`\n' +\
		'				decline\n'
	stock_template = '\n' +\
		'			label "stock loop %%"\n' +\
		'			branch "notnull %%"\n' +\
		'				"stock tendency %%" != 0\n' +\
		'			action\n' +\
		'				"stock tendency %%" = "roll: 3" - 1\n' +\
		'			branch "stock loop %%"\n' +\
		'			label "notnull %%"\n' +\
		'			action\n' +\
		'				"stock change %%" = "roll: 50" * "stock tendency %%"\n' +\
		'			branch "positive %%"\n' +\
		'				"stock value %%" + "stock change %%" >= 100\n' +\
		'			action\n' +\
		'				"stock change %%" *= -1\n' +\
		'			label "positive %%"\n' +\
		'			action\n' +\
		'				"stock value %%" += "stock change %%"\n'
	overview = '' +\
		'			`You hold &[stock amount %%] "%%" stocks at &[stock value %%] credits each. Dividend(3%): &[dividend %%]`\n' +\
		'				to display\n' +\
		'					"stock amount %%" > 0\n'
	tooffer = '		or\n'
	tendencyroll = ''
	stocktemplates = ''
	dividends = ''
	dividendsaddi = '				"stock dividends addi" = '
	setoverview = ''
	for i in range(0, len(stocks)):
		splitted = stocks[i].split('|')
		tooffer += '			"stock amount ' + splitted[0] + '" > 0\n'
		tendencyroll += '				"stock tendency ' + splitted[0] + '" = "roll: 3" - 1\n'
		stocktemplates += stock_template.replace('%%', splitted[0]).replace('%value%', splitted[1]) + '\n'
		dividends += '				"dividend ' + splitted[0] + '" = "stock amount ' + splitted[0] + '" * "stock value ' + splitted[0] + '" / 100 * 3\n'
		if i == len(stocks) -1:
			dividendsaddi += '"dividend ' + splitted[0] + '"\n'
		else:
			dividendsaddi += '"dividend ' + splitted[0] + '" + '
		setoverview += overview.replace('%%', splitted[0]).replace('%value%', splitted[1])
	mission2 = mission2.replace('%tooffer%', tooffer)
	mission2 = mission2.replace('%tendencyroll%', tendencyroll)
	mission2 = mission2.replace('%stocktemplates%', stocktemplates)
	mission2 = mission2.replace('%dividends%', dividends)
	mission2 = mission2.replace('%dividendsaddi%', dividendsaddi)
	mission2 = mission2.replace('%overview%', setoverview)
	return mission2 


def create_mission3(stocks, mission1, mission2, stuff):
	mission3calc = '' +\
		'			action\n' +\
		'				"passed days" = "days since start" - "stock last day"\n' +\
		'			label "calculations loop"\n' +\
		'			branch "calculations end"\n' +\
		'				"passed days" == 0\n' +\
		'			action\n' +\
		'%tendencyroll%' +\
		'%stocktemplates%' +\
		'			action\n' +\
		'				"passed days" -= 1\n' +\
		'			branch "calculations loop"\n' +\
		'			label "calculations end"\n' +\
		'			action\n' +\
		'				"stock last day" = "days since start"\n'
	mission3stocks = '' +\
		'			label "linestockoverview"\n' +\
		'			``\n' +\
		'			label "stockoverview"\n' +\
		'			action\n' +\
		'%stocktotalvalue%' +\
		'			scene "scene/stock_chart_analysis"\n' +\
		'			`Welcome to Galactic Stock Exchange`\n' +\
		'			``\n' +\
		'			`Cash chip balance: &[credits]`\n' +\
		'			`Value of all owned stocks: &[stocktotalvalue] credits`\n' +\
		'			``\n' +\
		'			choice\n' +\
		'%choicestocks%' +\
		'				`	[back]`\n' +\
		'					goto clearscreen\n' +\
		'%choicesinglestock%' +\
		'%labelstocks%' +\
		'%realselling%'
	choicesinglestocktemplate = '' +\
		'			label "line%%"\n' +\
		'			``\n' +\
		'			label "%%"\n' +\
		'			action\n' +\
		'				"stock value %% 1000000" = "stock value %%" * 1000000\n' +\
		'				"stock value %% 100000" = "stock value %%" * 100000\n' +\
		'				"stock value %% 10000" = "stock value %%" * 10000\n' +\
		'				"stock value %% 1000" = "stock value %%" * 1000\n' +\
		'				"stock value %% 100" = "stock value %%" * 100\n' +\
		'				"stock value %% 10" = "stock value %%" * 10\n' +\
		'			action\n' +\
		'%stocktotalvalue%' +\
		'			scene "scene/stock_chart_analysis"\n' +\
		'			`%%`\n' +\
		'			``\n' +\
		'			`Cash chip balance: &[credits] credits`\n' +\
		'			`Value of all owned stocks: &[stocktotalvalue] credits`\n' +\
		'			``\n' +\
		'			`You hold: &[stock amount %%] stocks at &[stock value %%] credits each..`\n' +\
		'			choice\n' +\
		'				`	Buy %% stocks`\n' +\
		'					to display\n' +\
		'						"credits" > "stock value %%"\n' +\
		'					goto "lineBuy %%"\n' +\
		'				`	Sell %% stocks`\n' +\
		'					to display\n' +\
		'						"stock amount %%" > 0\n' +\
		'					goto "lineSell %%"\n' +\
		'				`	[back]`\n' +\
		'					goto "linestockoverview"\n' +\
		'			label "lineBuy %%"\n' +\
		'			``\n' +\
		'			label "Buy %%"\n' +\
		'			scene "scene/stock_chart_analysis"\n' +\
		'			`%%`\n' +\
		'			``\n' +\
		'			`Cash chip balance: &[credits] credits`\n' +\
		'			`Value of all owned stocks: &[stocktotalvalue] credits`\n' +\
		'			``\n' +\
		'			`You hold: &[stock amount %%] stocks at &[stock value %%] credits each.`\n' +\
		'			choice\n' +\
		'				`	Buy 1,000,000 stocks for &[stock value %% 1000000] credits.`\n' +\
		'					to display\n' +\
		'						"credits" > "stock value %%" * 1000000\n' +\
		'					goto "Buy 1000000 %%"\n' +\
		'				`	Buy 100,000 stocks for &[stock value %% 100000] credits.`\n' +\
		'					to display\n' +\
		'						"credits" > "stock value %%" * 100000\n' +\
		'					goto "Buy 100000 %%"\n' +\
		'				`	Buy 10,000 stocks for &[stock value %% 10000] credits.`\n' +\
		'					to display\n' +\
		'						"credits" > "stock value %%" * 10000\n' +\
		'					goto "Buy 100000 %%"\n' +\
		'				`	Buy 1,000 stocks for &[stock value %% 1000] credits.`\n' +\
		'					to display\n' +\
		'						"credits" > "stock value %%" * 1000\n' +\
		'					goto "Buy 1000 %%"\n' +\
		'				`	Buy 100 stocks for &[stock value %% 100] credits.`\n' +\
		'					to display\n' +\
		'						"credits" > "stock value %%" * 100\n' +\
		'					goto "Buy 100 %%"\n' +\
		'				`	Buy 10 stocks for &[stock value %% 10] credits.`\n' +\
		'					to display\n' +\
		'						"credits" > "stock value %%" * 10\n' +\
		'					goto "Buy 10 %%"\n' +\
		'				`	Buy 1 stock for &[stock value %%] credits.`\n' +\
		'					to display\n' +\
		'						"credits" > "stock value %%" * 1\n' +\
		'					goto "Buy 1 %%"\n' +\
		'				`	[back]`\n' +\
		'					goto "line%%"\n' +\
		'			label "lineSell %%"\n' +\
		'			``\n' +\
		'			label "Sell %%"\n' +\
		'			scene "scene/stock_chart_analysis"\n' +\
		'			`%%`\n' +\
		'			``\n' +\
		'			`Cash chip balance: &[credits] credits`\n' +\
		'			`Value of all owned stocks: &[stocktotalvalue] credits`\n' +\
		'			``\n' +\
		'			`You hold: &[stock amount %%] stocks at &[stock value %%] credits each.`\n' +\
		'			choice\n' +\
		'				`	Sell 1,000,000 stocks for &[stock value %% 1000000] credits.`\n' +\
		'					to display\n' +\
		'						"stock amount %%" >= 1000000\n' +\
		'					goto "Sell 1000000 %%"\n' +\
		'				`	Sell 100,000 stocks for &[stock value %% 100000] credits.`\n' +\
		'					to display\n' +\
		'						"stock amount %%" >= 100000\n' +\
		'					goto "Sell 100000 %%"\n' +\
		'				`	Sell 10,000 stocks for &[stock value %% 10000] credits.`\n' +\
		'					to display\n' +\
		'						"stock amount %%" >= 10000\n' +\
		'					goto "Sell 10000 %%"\n' +\
		'				`	Sell 1,000 stocks for &[stock value %% 1000] credits.`\n' +\
		'					to display\n' +\
		'						"stock amount %%" >= 1000\n' +\
		'					goto "Sell 1000 %%"\n' +\
		'				`	Sell 100 stocks for &[stock value %% 100] credits.`\n' +\
		'					to display\n' +\
		'						"stock amount %%" >= 100\n' +\
		'					goto "Sell 100 %%"\n' +\
		'				`	Sell 10 stocks for &[stock value %% 10] credits.`\n' +\
		'					to display\n' +\
		'						"stock amount %%" >= 10\n' +\
		'					goto "Sell 10 %%"\n' +\
		'				`	Sell 1 stock for &[stock value %%] credits.`\n' +\
		'					to display\n' +\
		'						"stock amount %%" >= 1\n' +\
		'					goto "Sell 1 %%"\n' +\
		'				`	[back]`\n' +\
		'					goto "line%%"\n'
	stock_template = '\n' +\
		'			label "stock loop %%"\n' +\
		'			branch "notnull %%"\n' +\
		'				"stock tendency %%" != 0\n' +\
		'			action\n' +\
		'				"stock tendency %%" = "roll: 3" - 1\n' +\
		'			branch "stock loop %%"\n' +\
		'			label "notnull %%"\n' +\
		'			action\n' +\
		'				"stock change %%" = "roll: 50" * "stock tendency %%"\n' +\
		'			branch "positive %%"\n' +\
		'				"stock value %%" + "stock change %%" >= 100\n' +\
		'			action\n' +\
		'				"stock change %%" *= -1\n' +\
		'			label "positive %%"\n' +\
		'			action\n' +\
		'				"stock value %%" += "stock change %%"\n'
	labelstocktemplate = '' +\
		'			label "Buy 1000000 %%"\n' +\
		'			action\n' +\
		'				"price" = "stock value %%" * 1000000\n' +\
		'				"stock amount %%" += 1000000\n' +\
		'			`Bought 1,000,000 %%`\n' +\
		'				goto "buy stocks %%"\n' +\
		'			label "Buy 100000 %%"\n' +\
		'			action\n' +\
		'				"price" = "stock value %%" * 100000\n' +\
		'				"stock amount %%" += 100000\n' +\
		'			`Bought 100,000 %%`\n' +\
		'				goto "buy stocks %%"\n' +\
		'			label "Buy 10000 %%"\n' +\
		'			action\n' +\
		'				"price" = "stock value %%" * 10000\n' +\
		'				"stock amount %%" += 10000\n' +\
		'			`Bought 10,000 %%`\n' +\
		'				goto "buy stocks %%"\n' +\
		'			label "Buy 1000 %%"\n' +\
		'			action\n' +\
		'				"price" = "stock value %%" * 1000\n' +\
		'				"stock amount %%" += 1000\n' +\
		'			`Bought 1,000 %%`\n' +\
		'				goto "buy stocks %%"\n' +\
		'			label "Buy 100 %%"\n' +\
		'			action\n' +\
		'				"price" = "stock value %%" * 100\n' +\
		'				"stock amount %%" += 100\n' +\
		'			`Bought 100 %%`\n' +\
		'				goto "buy stocks %%"\n' +\
		'			label "Buy 10 %%"\n' +\
		'			action\n' +\
		'				"price" = "stock value %%" * 10\n' +\
		'				"stock amount %%" += 10\n' +\
		'			`Bought 10 %%`\n' +\
		'				goto "buy stocks %%"\n' +\
		'			label "Buy 1 %%"\n' +\
		'			action\n' +\
		'				"price" = "stock value %%" * 1\n' +\
		'				"stock amount %%" += 1\n' +\
		'			`Bought 1 %%`\n' +\
		'				goto "buy stocks %%"\n' +\
		'			label "Sell 1000000 %%"\n' +\
		'			action\n' +\
		'				"price" = "stock value %%" * 1000000\n' +\
		'				"stock amount %%" -= 1000000\n' +\
		'			`Sold 1,000,000 %%`\n' +\
		'				goto "sell stocks %%"\n' +\
		'			label "Sell 100000 %%"\n' +\
		'			action\n' +\
		'				"price" = "stock value %%" * 100000\n' +\
		'				"stock amount %%" -= 100000\n' +\
		'			`Sold 100,000 %%`\n' +\
		'				goto "sell stocks %%"\n' +\
		'			label "Sell 10000 %%"\n' +\
		'			action\n' +\
		'				"price" = "stock value %%" * 10000\n' +\
		'				"stock amount %%" -= 10000\n' +\
		'			`Sold 10000 %%`\n' +\
		'				goto "sell stocks %%"\n' +\
		'			label "Sell 1000 %%"\n' +\
		'			action\n' +\
		'				"price" = "stock value %%" * 1000\n' +\
		'				"stock amount %%" -= 1000\n' +\
		'			`Sold 1000 %%`\n' +\
		'				goto "sell stocks %%"\n' +\
		'			label "Sell 100 %%"\n' +\
		'			action\n' +\
		'				"price" = "stock value %%" * 100\n' +\
		'				"stock amount %%" -= 100\n' +\
		'			`Sold 100 %%`\n' +\
		'				goto "sell stocks %%"\n' +\
		'			label "Sell 10 %%"\n' +\
		'			action\n' +\
		'				"price" = "stock value %%" * 10\n' +\
		'				"stock amount %%" -= 10\n' +\
		'			`Sold 10 %%`\n' +\
		'				goto "sell stocks %%"\n' +\
		'			label "Sell 1 %%"\n' +\
		'			action\n' +\
		'				"price" = "stock value %%"\n' +\
		'				"stock amount %%" -= 1\n' +\
		'			`Sold 1 %%`\n' +\
		'				goto "sell stocks %%"\n'
	realsellingtemplate = '' +\
		'			label "buy stocks %%"\n' +\
		'			label "buy stocks 1000000 %%"\n' +\
		'			branch "buy stocks 100000 %%"\n' +\
		'				"price" < 1000000\n' +\
		'			action\n' +\
		'				payment -1000000\n' +\
		'				price -= 1000000\n' +\
		'			branch "buy stocks 1000000 %%"\n' +\
		'			label "buy stocks 100000 %%"\n' +\
		'			branch "buy stocks 10000 %%"\n' +\
		'				"price" < 100000\n' +\
		'			action\n' +\
		'				payment -100000\n' +\
		'				price -= 100000\n' +\
		'			branch "buy stocks 100000 %%"\n' +\
		'			label "buy stocks 10000 %%"\n' +\
		'			branch "buy stocks 1000 %%"\n' +\
		'				"price" < 10000\n' +\
		'			action\n' +\
		'				payment -10000\n' +\
		'				price -= 10000\n' +\
		'			branch "buy stocks 10000 %%"\n' +\
		'			label "buy stocks 1000 %%"\n' +\
		'			branch "buy stocks 100 %%"\n' +\
		'				"price" < 1000\n' +\
		'			action\n' +\
		'				payment -1000\n' +\
		'				price -= 1000\n' +\
		'			branch "buy stocks 1000 %%"\n' +\
		'			label "buy stocks 100 %%"\n' +\
		'			branch "buy stocks 10 %%"\n' +\
		'				"price" < 100\n' +\
		'			action\n' +\
		'				payment -100\n' +\
		'				price -= 100\n' +\
		'			branch "buy stocks 100 %%"\n' +\
		'			label "buy stocks 10 %%"\n' +\
		'			branch "buy stocks 1 %%"\n' +\
		'				"price" < 10\n' +\
		'			action\n' +\
		'				payment -10\n' +\
		'				price -= 10\n' +\
		'			branch "buy stocks 10 %%"\n' +\
		'			label "buy stocks 1 %%"\n' +\
		'			branch "buy stocks end %%"\n' +\
		'				"price" < 1\n' +\
		'			action\n' +\
		'				payment -1\n' +\
		'				price -= 1\n' +\
		'			branch "buy stocks 1 %%"\n' +\
		'\n' +\
		'			label "buy stocks end %%"\n' +\
		'			branch "Buy %%"\n' +\
		'\n' +\
		'			label "sell stocks %%"\n' +\
		'\n' +\
		'			label "sell stocks 1000000 %%"\n' +\
		'			branch "sell stocks 100000 %%"\n' +\
		'				"price" < 1000000\n' +\
		'			action\n' +\
		'				payment +1000000\n' +\
		'				price -= 1000000\n' +\
		'			branch "sell stocks 100000 %%"\n' +\
		'			label "sell stocks 100000 %%"\n' +\
		'			branch "sell stocks 10000 %%"\n' +\
		'				"price" < 100000\n' +\
		'			action\n' +\
		'				payment +100000\n' +\
		'				price -= 100000\n' +\
		'			branch "sell stocks 100000 %%"\n' +\
		'			label "sell stocks 10000 %%"\n' +\
		'			branch "sell stocks 1000 %%"\n' +\
		'				"price" < 10000\n' +\
		'			action\n' +\
		'				payment +10000\n' +\
		'				price -= 10000\n' +\
		'			branch "sell stocks 10000 %%"\n' +\
		'			label "sell stocks 1000 %%"\n' +\
		'			branch "sell stocks 100 %%"\n' +\
		'				"price" < 1000\n' +\
		'			action\n' +\
		'				payment +1000\n' +\
		'				price -= 1000\n' +\
		'			branch "sell stocks 1000 %%"\n' +\
		'			label "sell stocks 100 %%"\n' +\
		'			branch "sell stocks 10 %%"\n' +\
		'				"price" < 100\n' +\
		'			action\n' +\
		'				payment +100\n' +\
		'				price -= 100\n' +\
		'			branch "sell stocks 100 %%"\n' +\
		'			label "sell stocks 10 %%"\n' +\
		'			branch "sell stocks 1 %%"\n' +\
		'				"price" < 10\n' +\
		'			action\n' +\
		'				payment +10\n' +\
		'				price -= 10\n' +\
		'			branch "sell stocks 10 %%"\n' +\
		'			label "sell stocks 1 %%"\n' +\
		'			branch "sell stocks end %%"\n' +\
		'				"price" < 1\n' +\
		'			action\n' +\
		'				payment +1\n' +\
		'				price -= 1\n' +\
		'			branch "sell stocks 1 %%"\n' +\
		'\n' +\
		'			label "sell stocks end %%"\n' +\
		'			branch "Sell %%"\n'
	showstocks = ''
	choicestocks = ''
	choicesinglestock = ''
	labelstocks = ''
	realselling = ''
	tendencyroll = ''
	stocktotalvalue = '				stocktotalvalue ='
	stocktemplates = ''
	for i in range(0, len(stocks)):
		splitted = stocks[i].split('|')
		tendencyroll += '				"stock tendency ' + splitted[0] + '" = "roll: 3" - 1\n'
		stocktemplates += stock_template.replace('%%', splitted[0]).replace('%value%', splitted[1]) + '\n'
		if i == len(stocks) - 1:
			stocktotalvalue += ' "stock amount ' + splitted[0] + '" * "stock value ' + splitted[0] + '"\n'
		else:
			stocktotalvalue += ' "stock amount ' + splitted[0] + '" * "stock value ' + splitted[0] + '" +'
		choicestocks += '				`	Trade "' + splitted[0] + '" stocks at &[stock value ' + splitted[0] + '] credits each. You hold &[stock amount ' + splitted[0] + '].`\n' +\
			'					goto "line' + splitted[0] + '"\n'
		choicesinglestock += choicesinglestocktemplate.replace('%%', splitted[0])
		labelstocks += labelstocktemplate.replace('%%', splitted[0])
		realselling += realsellingtemplate.replace('%%', splitted[0])
	mission3calc = mission3calc.replace('%tendencyroll%', tendencyroll)
	mission3calc = mission3calc.replace('%stocktemplates%', stocktemplates)
	mission3stocks = mission3stocks.replace('%choicestocks%', choicestocks)
	mission3stocks = mission3stocks.replace('%choicesinglestock%', choicesinglestock)
	mission3stocks = mission3stocks.replace('%labelstocks%', labelstocks)
	mission3stocks = mission3stocks.replace('%realselling%', realselling)
	mission3stocks = mission3stocks.replace('%stocktotalvalue%', stocktotalvalue)
	# put texts together and write to file				
	with open('banking_template.txt', 'r') as s:
		template = s.read()
	template = template.replace('%othermissions%', mission1 + '\n' + mission2 + '\n')
	template = template.replace('%stockcalculations%', mission3calc)
	template = template.replace('%stockexchange%', mission3stocks)
	template = template.replace('%comments%', stuff)
	template = template.replace('%stocktotalvalue%', stocktotalvalue)
	with open('gci_banking.txt', 'w') as t:
		t.writelines(template)




if __name__ == "__main__":
	stocks = ['Southbound Shipyards|1322',
		'Lionheart Shipyards|976', 
		'Megaparsec Shipyards|1110',
		'Syndicate Shipyards|1692',
		'Kraz Cybernetics|1451',
		'Deep Sky|837',
		'Lovelace Labs|1791',
		'Delta V|788',
		'Betelgeuse Shipyards|1224',
		'Tarazed Corporation|676']
	stuff = '' +\
		'# mission "gci stock setup"\n' +\
		'# mission "gci stock dividends"'
	mission1 = create_mission1(stocks)
	mission2 = create_mission2(stocks)
	create_mission3(stocks, mission1, mission2, stuff)