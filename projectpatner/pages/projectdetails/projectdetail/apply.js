// pages/projectdetails/projectdetail/apply.js
Page({

  /**
   * 页面的初始数据
   */
  data: {

  },

  goBack: function() {
    // 实现返回功能
    wx.navigateBack();
  },

  applyJoin: function() {
    // 实现申请加入的逻辑
    wx.showToast({
      title: '申请已提交',
      icon: 'success',
      duration: 2000
    });
    setTimeout(() => {
      wx.navigateBack();
    }, 2000);
  },
})