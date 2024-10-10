// pages/log/log.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    users: [],
    username: '',
    password: ''
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function() {
    // 加载用户信息
    const app = getApp();
    this.setData({
      users: app.globalData.users
    });
  },
  inputUsername: function(e) {
    this.setData({
      username: e.detail.value
    });
  },
  inputPassword: function(e) {
    this.setData({
      password: e.detail.value
    });
  },
  login() {
    // 这里应该调用后端API进行登录验证
    // 以下是示例代码，假设登录成功
    if (this.data.username && this.data.password) {
      const app = getApp();
    const { users, username, password } = this.data;
    const user = users.find(u => u.username === username && u.password === password);

    if (user) {
      // 登录成功，保存当前用户信息到全局数据和本地存储
      app.globalData.currentUser = user;
      wx.setStorageSync('currentUser', user);
      // 跳转到首页
      wx.switchTab({
        url: '/pages/home/home',
      })
    } else {
      // 登录失败，显示错误提示
      wx.showToast({
        title: '账号或密码错误',
        icon: 'none',
        duration: 2000
      });
    }
    } else {
      wx.showToast({
        title: '请填写用户名和密码',
        icon: 'none'
      });
    }
  },
})