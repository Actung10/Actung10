// pages/projectdetails/joinedproject/joinedproject.js
Page({
  data: {
    project: {}, // 当前项目详情
    currentTab: 'projectDetails', // 默认显示的项目详情
  },

  onLoad: function(options) {
    // 获取传递过来的项目ID
    const projectId = parseInt(options.projectId, 10);
    const app = getApp();
    const allProjects = app.globalData.projects;
    const project = allProjects.find(p => p.id === projectId);

    if (project) {
      // 设置项目详情数据
      this.setData({
        project: {
          id: project.id,
          name: project.name,
          introduction: project.introduction,
          content: project.content,
          mentor: project.mentor,
          initiator: project.initiator,
          currentMembersCount: project.members.length,
          totalMembers: project.totalMembers || project.currentMembersCount, // 假设项目总成员数未定义则与当前成员数相同
          status: project.status,
          members: project.members // 确保 members 数组被正确赋值
        },
      });
    } else {
      // 如果没有找到项目，显示错误信息
      wx.showToast({
        title: '项目不存在',
        icon: 'none',
      });
      wx.navigateBack({
        delta: 1,
      });
    }
  },

  // 生命周期函数--监听页面显示
  onShow: function() {
    // 重新获取全局数据中的当前项目信息
    const app = getApp();
    const options = this.options; // 从页面实例中获取传递的参数对象
    const projectId = parseInt(options.projectId, 10); // 获取传递的项目ID
    const project = app.globalData.projects.find(p => p.id === projectId);

    if (project) {
      // 设置项目详情数据
      this.setData({
        project: {
          id: project.id,
          name: project.name,
          introduction: project.introduction,
          content: project.content,
          mentor: project.mentor,
          initiator: project.initiator,
          currentMembersCount: project.members.length,
          totalMembers: project.totalMembers || project.currentMembersCount, // 假设项目总成员数未定义则与当前成员数相同
          status: project.status,
          members: project.members // 确保 members 数组被正确赋值
        },
      });
    } else {
      // 如果没有找到项目，显示错误信息并返回上一页
      wx.showToast({
        title: '项目不存在',
        icon: 'none',
      });
      setTimeout(() => {
        wx.navigateBack({
          delta: 1,
        });
      }, 1500); // 延迟1.5秒后返回上一页
    }
  },

  switchTab: function(e) {
    const type = e.currentTarget.dataset.type;
    this.setData({
      currentTab: type
    });
  },
  goBack: function() {
    // 实现返回功能
    wx.navigateBack();
  },
  intogroup: function() {
    // 实现申请加入的逻辑
    wx.showToast({
      title: '进入群聊',
      icon: 'success',
      duration: 2000
    });
  },
  // ...其他数据和方法...

  exitProject: function() {
    // 显示提示框
    wx.showModal({
      title: '退出项目',
      content: '确定退出项目吗？',
      success: (res) => {
        if (res.confirm) {
          console.log('用户点击确定');
          // 这里执行退出项目的操作
          // 例如，调用API删除项目或者将用户从项目中移除
          // 完成后可以返回上一页或者跳转到其他页面
          wx.navigateBack();
        } 
      }
    });
  },

});