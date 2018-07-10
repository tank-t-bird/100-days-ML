using System.Collections.Generic;
using UnityEngine;

public class TransformationGrid : MonoBehaviour
{
	public Transform Prefab;
	public int GridResolution = 10;
	private Transform[ ] _grid;
	private List<Transformation> _transformations;
	private Matrix4x4 _transformation;

	private void Awake()
	{
		_grid = new Transform[GridResolution * GridResolution * GridResolution];
		for (int i = 0, z = 0; z < GridResolution; z++)
		{
			for (int y = 0; y < GridResolution; y++)
			{
				for (int x = 0; x < GridResolution; x++, i++)
				{
					_grid[i] = CreateGridPoint(x, y, z);
				}
					
			}
		}

		_transformations = new List<Transformation>();
	}

	private Transform CreateGridPoint(int x, int y, int z)
	{
		Transform point = Instantiate(Prefab);
		point.localPosition = GetCoordinates(x, y, z);
		point.GetComponent<MeshRenderer>().material.color = new Color(
			(float)x / GridResolution,
			(float)y / GridResolution,
			(float)z / GridResolution
			);
		return point;

	}

	//this builds the coordiantes around the center
	private Vector3 GetCoordinates(int x, int y, int z) 
	{
		return new Vector3(
			x - (GridResolution - 1) * 0.5f,
			y - (GridResolution - 1) * 0.5f,
			z - (GridResolution - 1) * 0.5f
		);
	}
	
	void Update ()
	{
		UpdateTransformation();
		for (int i = 0, z = 0; z < GridResolution; z++) {
			for (int y = 0; y < GridResolution; y++) {
				for (int x = 0; x < GridResolution; x++, i++) {
					_grid[i].localPosition = TransformPoint(x, y, z);
				}
			}
		}
	}

	void UpdateTransformation()
	{
		GetComponents<Transformation>(_transformations);
		if (_transformations.Count > 0)
		{
			_transformation = _transformations[0].Matrix;
			for (int i = 1; i < _transformations.Count; i++)
			{
				_transformation = _transformations[i].Matrix * _transformation;
			}
		}
	}
	
	Vector3 TransformPoint (int x, int y, int z) {
		Vector3 coordinates = GetCoordinates(x, y, z);
		return _transformation.MultiplyPoint(coordinates);
	}
}
