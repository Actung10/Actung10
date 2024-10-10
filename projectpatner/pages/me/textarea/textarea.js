Page({
  data: {
    memo: '' // 用于存储备忘录内容
  },
  onLoad: function() {
    // 页面加载时，从本地存储中读取备忘录内容
    const savedMemo = wx.getStorageSync('memo') || '';
    this.setData({
      memo: savedMemo
    });
  },
  onInput: function(e) {
    // 当输入框内容变化时，更新数据
    this.setData({
      memo: e.detail.value
    });
  },
  onBlur: function() {
    // 当输入框失去焦点时，保存内容到本地存储
    wx.setStorageSync('memo', this.data.memo);
  },
  goBack: function() {
    // 返回按钮的事件处理函数
    wx.navigateBack({
      delta: 1
    });
  }
});
