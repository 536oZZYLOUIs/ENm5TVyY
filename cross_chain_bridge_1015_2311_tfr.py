# 代码生成时间: 2025-10-15 23:11:38
import streamlit as st
import json
from typing import Dict, Any

# 模拟区块链数据结构
class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.nodes = set()

    def add_block(self, previous_hash, proof):
        """
        添加新区块到链上
        :param previous_hash: 上一个区块的哈希值
        :param proof: 工作量证明算法的证明
        """
        # 创建新区块
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }
        # 重置当前交易列表
        self.current_transactions = []
        # 添加区块到链
        self.chain.append(block)
        return block

    def add_transaction(self, sender, recipient, amount):
        """
        添加交易到列表
        :param sender: 发送者地址
        :param recipient: 接收者地址
        :param amount: 交易金额
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
        return self.last_block['index'] + 1

    def hash(self, block):
        """
        创建区块的哈希值
        :param block: 区块对象
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

# 跨链桥接工具类
class CrossChainBridge:
    def __init__(self, blockchains: Dict[str, Blockchain]):
        self.blockchains = blockchains

    def send_transaction(self, sender, recipient, amount, blockchain_name):
        """
        发送跨链交易
        :param sender: 发送者地址
        :param recipient: 接收者地址
        :param amount: 交易金额
        :param blockchain_name: 区块链名称
        """
        try:
            # 添加交易到指定区块链
            new_index = self.blockchains[blockchain_name].add_transaction(sender, recipient, amount)
            st.success(f'Transaction will be added to block {new_index}')
        except Exception as e:
            st.error(f'Failed to add transaction: {e}')

    def display_chain(self, blockchain_name):
        """
        显示指定区块链的链信息
        :param blockchain_name: 区块链名称
        """
        chain = self.blockchains[blockchain_name].chain
        st.json(chain)

# Streamlit 应用
if __name__ == '__main__':
    # 创建两个区块链实例
    blockchain_a = Blockchain()
    blockchain_b = Blockchain()

    # 创建跨链桥接工具实例
    cross_chain_bridge = CrossChainBridge({'blockchain_a': blockchain_a, 'blockchain_b': blockchain_b})

    # Streamlit 页面设置
    st.title('Cross Chain Bridge Tool')

    # 选择区块链
    blockchain_name = st.selectbox(
        'Select a blockchain to interact with:',
        ['blockchain_a', 'blockchain_b']
    )

    # 发送交易
    sender = st.text_input('Sender Address')
    recipient = st.text_input('Recipient Address')
    amount = st.number_input('Amount', value=0.0, step=0.1)
    if st.button('Send Transaction'):
        cross_chain_bridge.send_transaction(sender, recipient, amount, blockchain_name)

    # 显示链信息
    if st.button('Display Chain'):
        cross_chain_bridge.display_chain(blockchain_name)