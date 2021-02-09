import vtk
from VtkAdapter import Draw
from calcTriangles import CustomTrianglesProvider, calctriangles
from StateTable import StateTable

calctriangles()

eps = 10 ** -8

colors = vtk.vtkNamedColors()
renderer = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(renderer)

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(renWin)
top = 0

Draw.Line(renderer, (StateTable.start * 1.5, 0, 0), (StateTable.end * 1.5, 0, 0), 'X')
Draw.Line(renderer, (0, StateTable.start * 1.5, 0), (0, StateTable.end * 1.5, 0), 'Y')
Draw.Line(renderer, (0, 0, StateTable.start * 1.5), (0, 0, StateTable.end * 1.5), 'Z')

for triangle in CustomTrianglesProvider.triangles:
    Draw.AddTriangle(*triangle)



print(len(CustomTrianglesProvider.triangles))

colors = vtk.vtkNamedColors()
trianglePolyData = vtk.vtkPolyData()
trianglePolyData.SetPoints(Draw.vtkpoints)
trianglePolyData.SetPolys(Draw.vtktriangles)
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputData(trianglePolyData)
actor = vtk.vtkActor()
actor.GetProperty().SetDiffuseColor(colors.GetColor3d("Blue"))
actor.GetProperty().SetAmbientColor(colors.GetColor3d("Red"))
actor.GetProperty().SetSpecularColor(colors.GetColor3d("Red"))
actor.GetProperty().SetSpecular(0.6)
actor.GetProperty().SetSpecularPower(30)
camera = vtk.vtkCamera()
camera.SetPosition(0, 0, 100)
camera.SetFocalPoint(0, 0, 0)


actor.SetMapper(mapper)
renderer.AddActor(actor)
renderer.SetActiveCamera(camera)

renderer.SetBackground(colors.GetColor3d("Tan"))
renWin.SetSize(1920, 1080)
interactor.Initialize()
renderer.ResetCamera()
renderer.GetActiveCamera().Zoom(1.5)
renWin.Render()
interactor.Start()
