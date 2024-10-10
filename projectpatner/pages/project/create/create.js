// pages/project/create/create.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    projectName: '',
    projectIntroduction: '',
    projectContent: '',
    mentor: '',
    projectMembers: ''
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady() {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow() {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide() {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload() {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh() {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom() {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage() {

  },
  inputProjectName(e) {
    this.setData({
      projectName: e.detail.value
    });
  },
  inputProjectIntroduction(e) {
    this.setData({
      projectIntroduction: e.detail.value
    });
  },
  inputProjectContent(e) {
    this.setData({
      projectContent: e.detail.value
    });
  },
  inputMentor(e) {
    this.setData({
      mentor: e.detail.value
    });
  },
  inputProjectMembers(e) {
    this.setData({
      projectMembers: e.detail.value
    });
  },
  goBack() {
    wx.navigateBack({
      delta: 1
    });
  },
  publishProject: function() {
    const app = getApp();
    // 提前声明 currentUser 变量
    const currentUser = app.globalData.users.find(user => user.name === app.globalData.currentUser.name);
  
    const newProject = {
      id: app.globalData.projects.length + 1, // 使用当前项目数量加1作为新项目的ID
      name: this.data.projectName,
      introduction: this.data.projectIntroduction,
      content: this.data.projectContent,
      mentor: this.data.mentor,
      members: [currentUser.name], // 初始成员只有当前用户
      currentMembersCount: 1,
      totalMembers:this.data.projectMembers,
      status: '招募人员', // 默认状态为招募中
      initiator: currentUser.name // 发起者为当前用户
    };
  
    if (this.data.projectName && this.data.projectIntroduction && this.data.projectContent && this.data.mentor && this.data.projectMembers) {
      // 发布项目的逻辑
      app.globalData.projects.push(newProject); // 添加到全局项目列表
      currentUser.createdProjects.push(newProject.id); // 添加到当前用户的createdProjects
  
      // 保存全局数据到本地存储
      wx.setStorageSync('projects', app.globalData.projects);
      wx.setStorageSync('users', app.globalData.users);
  
      // 返回先前的界面
      wx.navigateBack({
        delta: 1
      });
    } else {
      wx.showToast({
        title: '请填写所有内容',
        icon: 'none'
      });
    }
  }
})