﻿using UnityEngine;

public class CameraSquishPersp : Transformation {
	public float FocalLength = 1f;
	
	public override Matrix4x4 Matrix
	{
		get
		{
			Matrix4x4 matrix = new Matrix4x4();
			matrix.SetRow(0, new Vector4(FocalLength, 0f, 0f, 0f));
			matrix.SetRow(2, new Vector4(0f, FocalLength, 0f, 0f));
			matrix.SetRow(3, new Vector4(0f, 0f, 1f, 0f));
			return matrix;
		}
	}
}
