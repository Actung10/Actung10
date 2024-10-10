// pages/home/home.js
Page({
  mixins: [require('common')],
  /**
   * 页面的初始数据
   */
  data: {
    inputShowed: false,
    inputVal: '',
    isFocus: false,
    projects: [], // 全局项目列表
    currentUser: {}, // 当前用户信息
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function() {
    const app = getApp();
    this.setData({
      projects: app.globalData.projects,
      currentUser: app.globalData.currentUser, // 假设当前用户信息存储在全局变量中
    });
  },

  // 生命周期函数--监听页面显示
  onShow: function() {
    // 重新获取全局数据中的项目列表和当前用户信息
    const app = getApp();
    const projects = app.globalData.projects;
    const currentUser = app.globalData.currentUser;

    // 更新页面数据
    this.setData({
      projects: projects,
      currentUser: currentUser,
    });
  },

  showInput() {
    this.setData({
      inputShowed: true,
    });
  },
  blurInput() {
    this.setData({
      isFocus: false,
    });
  },
  hideInput() {
    this.setData({
      inputVal: '',
      inputShowed: false,
    });
  },
  clearInput() {
    this.setData({
      inputVal: '',
    });
  },
  inputTyping(e) {
    this.setData({
      inputVal: e.detail.value,
      isFocus: true,
    });
  },
  searchInput: function() {
    const inputVal = this.data.inputVal.trim().toLowerCase();
    if (!inputVal) {
      // 如果搜索框为空，则不进行搜索
      wx.showToast({
        title: '请输入搜索内容',
        icon: 'none'
      });
      return;
    }
    // 跳转到搜索结果页面，并传递搜索关键词
    wx.navigateTo({
      url: `/pages/search/search?query=${encodeURIComponent(inputVal)}`
    });
  },

  goToProjectDetail: function(e) {
    const projectId = e.currentTarget.dataset.id; // 获取项目ID
    const app = getApp();
    const currentUser = app.globalData.users.find(user => user.id === 1); // 假设当前用户ID为1

    // 检查项目是否由当前用户创建
    if (currentUser.createdProjects.includes(projectId)) {
      wx.navigateTo({
        url: `/pages/projectdetails/createdproject/createdproject?projectId=${projectId}`,
      });
    }
    // 检查项目是否由当前用户参与但不是创建的
    else if (currentUser.joinedProjects.includes(projectId) && !currentUser.createdProjects.includes(projectId)) {
      wx.navigateTo({
        url: `/pages/projectdetails/joinedproject/joinedproject?projectId=${projectId}`,
      });
    }
    // 如果都不是，则跳转到项目详情页
    else {
      wx.navigateTo({
        url: `/pages/projectdetails/projectdetail/projectdetail?projectId=${projectId}`,
      });
    }
  },
})
