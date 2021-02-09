import vtk

class Draw:
    vtkpoints = vtk.vtkPoints()
    vtktriangles = vtk.vtkCellArray()
    top = 0

    @staticmethod
    def Arrow():
        colors = vtk.vtkNamedColors()

        arrowSource = vtk.vtkArrowSource()
        # arrowSource.SetShaftRadius(0.01)
        # arrowSource.SetTipLength(.9)

        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(arrowSource.GetOutputPort())
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        renderer = vtk.vtkRenderer()
        renderWindow = vtk.vtkRenderWindow()
        renderWindow.SetWindowName("Arrow")
        renderWindow.AddRenderer(renderer)
        renderWindowInteractor = vtk.vtkRenderWindowInteractor()
        renderWindowInteractor.SetRenderWindow(renderWindow)

        renderer.AddActor(actor)
        renderer.SetBackground(colors.GetColor3d("MidnightBlue"))

    @staticmethod
    def Line(renderer, p1, p2, name):
        X = vtk.vtkLineSource()
        X.SetPoint1(*p1)
        X.SetPoint2(*p2)
        X.Update()
        XMapper = vtk.vtkPolyDataMapper()
        XMapper.SetInputConnection(X.GetOutputPort())
        XActor = vtk.vtkActor()
        XActor.SetMapper(XMapper)
        XActor.GetProperty().SetColor(0, 0, 0)
        textActor = vtk.vtkBillboardTextActor3D()
        textActor.SetInput(name)
        textActor.GetTextProperty().SetFontSize(20)
        textActor.GetTextProperty().SetColor(0, 0, 0)
        textActor.SetPosition(*p2)
        renderer.AddActor(XActor)
        renderer.AddActor(textActor)

    @staticmethod
    def AddTriangle(p1, p2, p3):
        Draw.vtkpoints.InsertNextPoint(*p1)
        Draw.vtkpoints.InsertNextPoint(*p2)
        Draw.vtkpoints.InsertNextPoint(*p3)
        Draw.top += 3
        triangle = vtk.vtkTriangle()
        triangle.GetPointIds().SetId(0, Draw.top - 1)
        triangle.GetPointIds().SetId(1, Draw.top - 2)
        triangle.GetPointIds().SetId(2, Draw.top - 3)
        Draw.vtktriangles.InsertNextCell(triangle)