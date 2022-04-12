def format_cointracking(data):
    """
    Format data to cointracking format
    """

    # Format
    # Type,	Buy, Cur.,	Sell,	Cur.,	Fee,	Cur.,	Exchange,	Group,	Comment	Date,	Tx-ID



    # Create new list with header
    formatted_data = [['Type', 'Buy', 'Cur.', 'Sell', 'Cur.', 'Fee', 'Cur.', 'Exchange', 'Group', 'Comment', 'Date', 'Tx-ID']]
    # Loop through data skipping header
    for row in data[1:]:
        # if row[0] is empty or ∑ break
        if row[0] == '' or row[0] == '∑':
            break

        out_type = ''
        out_buy = ''
        out_buy_cur = ''
        out_sell = ''
        out_sell_cur = ''
        out_fee = ''
        out_fee_cur = ''
        out_exchange = ''
        out_group = ''
        out_comment = ''
        out_date = ''
        out_txid = ''

        out_date = row[0]

        if row[1] == 'Hashpower mining':
            out_type = 'Mining'
            out_buy = row[2]
            out_buy_cur = 'BTC'
            out_exchange = 'Nicehash'
            out_group = 'Mining'

        elif row[1] == 'Withdrawal complete':
            out_type = 'Withdrawal'
            out_sell = abs(float(row[2]))
            out_sell_cur = 'BTC'
            out_exchange = 'Nicehash'
            out_group = 'Withdrawal'


    
        # if row[1] does not contain 'fee'
        if 'fee' not in row[1]:
            formatted_data.append(
                [out_type, out_buy, out_buy_cur, out_sell, out_sell_cur, out_fee, out_fee_cur,
                out_exchange, out_group, out_comment, out_date, out_txid]
            )

        elif 'fee' in row[1]:

            # go through formatted_data in reverse order
            for i in range(len(formatted_data)-1, -1, -1):
                if row[1] == 'Hashpower mining fee' and formatted_data[i][0] == "Mining" and row[0] == formatted_data[i][10]:
                    formatted_data[i][5] = abs(float(row[2]))
                    formatted_data[i][6] = 'BTC'
                    break
            
                # if first word of row[1] is withdrawal and matches first word of formatted_data
                if row[1] == 'Withdrawal fee' and formatted_data[i][0] == "Withdrawal" and row[0] == formatted_data[i][10]:
                    formatted_data[i][5] = abs(float(row[2]))
                    formatted_data[i][6] = 'BTC'
                    break





    return formatted_data

    
    
