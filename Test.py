# -*- coding: utf-8 -*-
# Author: zhangxinlei
# Time: 2021/7/31 12:03
import FbxCommon


def PrintAllNode(fbxNode):
	for i in range(fbxNode.GetChildCount()):
		childFbxNode = fbxNode.GetChild(i)
		print(fbxNode.GetName(), childFbxNode.GetName())
		for j in range(childFbxNode.GetMaterialCount()):
			material = childFbxNode.GetMaterial(j)
			print(material.GetName())
		PrintAllNode(childFbxNode)


if __name__ == '__main__':
	filename = "G:/Projects/S6/design/DATA/SceneEditor/Resources/Model/Cube.FBX"
	fbxManager, fbxScene = FbxCommon.InitializeSdkObjects()
	result = FbxCommon.LoadScene(fbxManager, fbxScene, filename)
	print(result)

	fbxRoot = fbxScene.GetRootNode()
	PrintAllNode(fbxRoot)
