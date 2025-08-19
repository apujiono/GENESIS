import json

class HelpEngine:
    def __init__(self):
        self.commands = {
            '/help': 'Show this help message.',
            '/start_mining [coin]': 'Start mining (e.g. /start_mining virai).',
            '/stake [amount]': 'Stake VIRAI (e.g. /stake 100).',
            '/swap [amount] [to_token]': 'Swap VIRAI (e.g. /swap 100 ETH).',
            '/generate_nft [data_type]': 'Generate NFT (e.g. /generate_nft analytics).',
            '/sell_nft [nft_id] [price]': 'Sell NFT (e.g. /sell_nft 123 500).',
            '/create_wallet': 'Create VIRAI wallet.',
            '/transfer [to_wallet] [amount]': 'Transfer VIRAI (e.g. /transfer wallet_address 10).',
            '/scan_network [target]': 'Scan network (e.g. /scan_network 192.168.1.1).',
            '/protect': 'Activate system protection.',
            '/run_tool [tool_name] [args]': 'Run security tool (e.g. /run_tool nmap -sV 192.168.1.1).',
            '/analytics': 'Show system analytics.',
            '/upgrade': 'Trigger system evolution.'
        }

    def get_help(self):
        response = "Yo, bro! Here's the list of commands:\n\n"
        for cmd, desc in self.commands.items():
            response += f"{cmd}: {desc}\n"
        response += "\nType them in the chat or use the buttons in Quick Actions. Have fun cuan-ing! 😎"
        return response
