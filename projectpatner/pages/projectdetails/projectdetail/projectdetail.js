// pages/projectdetails/projectdetail/projectdetail.js
Page({
  data: {
    project: {}, // 当前项目详情
  },

  onLoad: function(options) {
    const projectId = parseInt(options.projectId, 10); // 获取传递的项目ID
    const app = getApp();
    const allProjects = app.globalData.projects;
    const project = allProjects.find(p => p.id === projectId);

    if (project) {
      this.setData({
        project: {
          id:project.id,
          name: project.name,
          introduction: project.introduction,
          content: project.content,
          mentor: project.mentor,
          members:project.members,
          initiator: project.initiator,
          currentMembersCount: project.members.length,
          totalMembers: project.totalMembers || project.currentMembersCount, // 假设项目总成员数未定义则与当前成员数相同
          status: project.status,
        },
      });
    } else {
      wx.showToast({
        title: '项目不存在',
        icon: 'none',
      });
    }
  },
  // ... 其他数据和方法 ...

  goBack: function() {
    // 实现返回功能
    wx.navigateBack();
  },

  applyJoin: function() {
    wx.navigateTo({
      url: '/pages/projectdetails/projectdetail/apply',
    })
  },

  // ... 其他数据和方法 ...
});