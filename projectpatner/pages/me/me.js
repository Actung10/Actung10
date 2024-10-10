// pages/me/me.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    name: '', // 用户名
    signature: '', // 个签
    avatarUrl: '', // 用户头像地址
    projectCount: 0 // 参与项目数量
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {
    const app = getApp();
    // 假设你要加载的用户ID为1，这里需要根据实际情况来获取用户ID
    const currentUser = app.globalData.users.find(user => user.id === 1);
    if (currentUser) {
      this.setData({
        username: currentUser.name,
        signature: currentUser.signature,
        avatarUrl: currentUser.avatarUrl || '/static/tabbar/me.png', // 如果没有头像地址，默认使用一个地址
        projectCount: currentUser.joinedProjects.length + currentUser.createdProjects.length
      });
    }
  },

  // 生命周期函数--监听页面显示
  onShow: function() {
    const app = getApp();
    // 重新获取全局数据中的当前用户信息
    const currentUser = app.globalData.users.find(user => user.id === 1);
    if (currentUser) {
      // 更新页面数据
      this.setData({
        username: currentUser.name,
        signature: currentUser.signature,
        avatarUrl: currentUser.avatarUrl || '/static/tabbar/me.png', // 如果没有头像地址，默认使用一个地址
        projectCount: currentUser.joinedProjects.length + currentUser.createdProjects.length
      });
    }
  },

  editSignature: function() {
    wx.navigateTo({
      url: '/pages/editSignature/editSignature' // 跳转到编辑个签页面
    });
  },

  gotomemo(){
    console.log("yes");
    wx.navigateTo({
      url: '/pages/me/textarea/textarea',
    })
  },
})